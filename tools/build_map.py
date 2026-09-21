#!/usr/bin/env python3
"""
Regenerate the North Country map include and its pin coordinates.

The homepage map is a static inline SVG: 62 New York counties, each its own
<path>, with Lewis, Jefferson and St. Lawrence flagged for accent fill. Every
colour is a CSS variable, so the map follows the theme rather than baking one
in. There is no runtime JavaScript and no map library.

This script exists so the geometry is reproducible rather than hand-drawn. You
only need to run it if you are adding a pin in a town that is not already in
TOWNS, or changing the projection.

    python3 tools/build_map.py

Inputs : a US county GeoJSON (Census-derived, FIPS-keyed)
Outputs: _includes/north-country-map.html   (the SVG)
         _data/map_pins.yml                 (pin x/y in SVG user units)

Pins are edited by hand in _data/map_pins.yml afterwards. Re-running this
script rewrites the x/y for every town in TOWNS but leaves you to re-apply any
label/url edits, so read the diff before committing.
"""

import json
import math
import os
import sys

# --- Projection ------------------------------------------------------------
# Albers equal-area conic, tuned to New York State. A plate carree projection
# visibly shears a state this wide; Albers keeps the Lake Ontario shoreline and
# the St. Lawrence border reading correctly.
LAT0, LON0 = 42.5, -76.5          # projection origin
LAT1, LAT2 = 41.0, 44.0           # standard parallels

WIDTH = 960.0                      # SVG user units; height derives from bounds
PADDING = 12.0

# Counties rendered in the accent fill.
FOCUS = {"Lewis", "Jefferson", "St. Lawrence"}

# Douglas-Peucker tolerance in projected units. Raised until the file is small
# enough to inline without the shoreline going faceted.
TOLERANCE = 0.55

# Rings smaller than this (projected area) are dropped: river islands and
# sandbars that only add bytes at this size.
MIN_RING_AREA = 3.0

# Towns we place pins in, as (lat, lon). Add a row here, re-run, then edit
# _data/map_pins.yml. The extra North Country towns are pre-computed so a new
# client in one of them needs no Python at all.
TOWNS = {
    "Lowville": (43.7870, -75.4921),
    "Turin": (43.6317, -75.4149),
    "Watertown": (43.9748, -75.9108),
    "Carthage": (43.9776, -75.6088),
    "Croghan": (43.8942, -75.3921),
    "Boonville": (43.4834, -75.3352),
    "Canton": (44.5962, -75.1690),
    "Potsdam": (44.6698, -74.9813),
    "Massena": (44.9284, -74.8921),
    "Ogdensburg": (44.6942, -75.4863),
}


def albers(lon, lat):
    """Project lon/lat (degrees) to unscaled Albers x/y."""
    lon, lat = math.radians(lon), math.radians(lat)
    lon0, lat0 = math.radians(LON0), math.radians(LAT0)
    lat1, lat2 = math.radians(LAT1), math.radians(LAT2)

    n = 0.5 * (math.sin(lat1) + math.sin(lat2))
    c = math.cos(lat1) ** 2 + 2 * n * math.sin(lat1)
    rho0 = math.sqrt(c - 2 * n * math.sin(lat0)) / n
    rho = math.sqrt(c - 2 * n * math.sin(lat)) / n
    theta = n * (lon - lon0)
    return rho * math.sin(theta), rho0 - rho * math.cos(theta)


def perp_distance(pt, a, b):
    (x, y), (x1, y1), (x2, y2) = pt, a, b
    dx, dy = x2 - x1, y2 - y1
    if dx == 0 and dy == 0:
        return math.hypot(x - x1, y - y1)
    t = max(0.0, min(1.0, ((x - x1) * dx + (y - y1) * dy) / (dx * dx + dy * dy)))
    return math.hypot(x - (x1 + t * dx), y - (y1 + t * dy))


def simplify(points, tol):
    """Iterative Douglas-Peucker. Recursion blows the stack on long shorelines."""
    if len(points) < 3:
        return points
    keep = [False] * len(points)
    keep[0] = keep[-1] = True
    stack = [(0, len(points) - 1)]
    while stack:
        lo, hi = stack.pop()
        if hi - lo < 2:
            continue
        worst, worst_i = -1.0, lo
        for i in range(lo + 1, hi):
            d = perp_distance(points[i], points[lo], points[hi])
            if d > worst:
                worst, worst_i = d, i
        if worst > tol:
            keep[worst_i] = True
            stack.append((lo, worst_i))
            stack.append((worst_i, hi))
    return [p for p, k in zip(points, keep) if k]


def ring_area(ring):
    a = 0.0
    for i in range(len(ring) - 1):
        x1, y1 = ring[i]
        x2, y2 = ring[i + 1]
        a += x1 * y2 - x2 * y1
    return abs(a) / 2.0


def rings_of(geom):
    if geom["type"] == "Polygon":
        return list(geom["coordinates"])
    out = []
    for poly in geom["coordinates"]:
        out.extend(poly)
    return out


def main(src):
    with open(src) as fh:
        data = json.load(fh)

    counties = [f for f in data["features"] if f["properties"].get("STATE") == "36"]
    if len(counties) != 62:
        sys.exit("expected 62 NY counties, got %d" % len(counties))

    # Project everything first so we can compute shared bounds.
    projected = []
    for f in counties:
        name = f["properties"]["NAME"]
        rings = []
        for ring in rings_of(f["geometry"]):
            pts = [albers(lon, lat) for lon, lat in ring]
            rings.append(pts)
        projected.append((name, rings))

    xs = [x for _, rings in projected for r in rings for x, _ in r]
    ys = [y for _, rings in projected for r in rings for _, y in r]
    minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)

    scale = (WIDTH - 2 * PADDING) / (maxx - minx)
    height = (maxy - miny) * scale + 2 * PADDING

    def to_svg(pt):
        # SVG y grows downward and Albers y grows northward, so the y axis is
        # flipped here. Without this the state renders upside down.
        x, y = pt
        return ((x - minx) * scale + PADDING, (maxy - y) * scale + PADDING)

    paths = []
    for name, rings in sorted(projected, key=lambda t: t[0]):
        d_parts = []
        for ring in rings:
            pts = [to_svg(p) for p in ring]
            if ring_area(pts) < MIN_RING_AREA:
                continue
            pts = simplify(pts, TOLERANCE)
            if len(pts) < 3:
                continue
            d_parts.append(
                "M" + "L".join("%.1f %.1f" % (x, y) for x, y in pts) + "Z"
            )
        if not d_parts:
            continue
        focus = ' nc-county--focus' if name in FOCUS else ''
        paths.append(
            '    <path class="nc-county%s" d="%s"><title>%s County</title></path>'
            % (focus, "".join(d_parts), name)
        )

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Paths only. The <svg> wrapper and the pins live in
    # _includes/north-country-map.html, which is hand-maintained, so that
    # regenerating geometry never clobbers the pin list.
    out = os.path.join(root, "_includes", "nc-counties.svg.html")
    with open(out, "w") as fh:
        fh.write(PATHS_HEADER)
        fh.write("\n".join(paths))
        fh.write("\n")
    print("wrote %s (%.1f KB)" % (out, os.path.getsize(out) / 1024.0))

    meta = os.path.join(root, "_data", "map_meta.yml")
    with open(meta, "w") as fh:
        fh.write("# Generated by tools/build_map.py. The viewBox of the county\n")
        fh.write("# geometry in _includes/nc-counties.svg.html. Pin x/y in\n")
        fh.write("# _data/map_pins.yml are in these units.\n")
        fh.write("width: %.0f\n" % WIDTH)
        fh.write("height: %.1f\n" % height)
        fh.write("\n# Projected town coordinates. Copy an x/y from here when you add\n")
        fh.write("# a pin. A town that is not listed needs a row in TOWNS in\n")
        fh.write("# tools/build_map.py and a re-run.\n")
        fh.write("towns:\n")
        for town, (lat, lon) in sorted(TOWNS.items()):
            x, y = to_svg(albers(lon, lat))
            fh.write('  "%s": { x: %.1f, y: %.1f }\n' % (town, x, y))
    print("wrote %s" % meta)


PATHS_HEADER = '''<!-- Generated by tools/build_map.py - do not hand-edit.
     One <path> per New York county; Lewis, Jefferson and St. Lawrence
     carry .nc-county--focus. Wrapped by _includes/north-country-map.html. -->
'''


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "us-counties.json")
