---
# ─── Required front matter ───────────────────────────────────────────────
# `layout` is set automatically by _config.yml for everything in
# _case_studies/, so you can omit it. The collection permalink
# (/case-studies/:name/) is derived from this file's name, so this page
# renders at /case-studies/placeholder-with-images/
title: "Placeholder Case Study (with images)"
client: "Sample Client Co."
summary: "A template case study showing the exact front matter and image paths Jekyll needs to render."
description: "Used to validate the case-study layout and demonstrate how to reference image assets."

# ─── Optional hero image ─────────────────────────────────────────────────
# Path is site-relative; the layout pipes it through `relative_url` so it
# works under any baseurl. Drop real files into /assets/case-studies/.
hero_image: "/assets/case-studies/placeholder-hero.svg"
hero_image_alt: "Placeholder hero image for the sample case study"

# ─── Optional results grid ───────────────────────────────────────────────
results:
  - stat: "40%"
    label: "Faster turnaround after automation"
  - stat: "5 → 1"
    label: "Disconnected tools consolidated"
  - stat: "0"
    label: "Records lost between systems since launch"
---

This is a **placeholder case study** that demonstrates the format required for
Jekyll to render a page in the `case_studies` collection. Copy this file,
rename it, and replace the content to publish a real story.

## How images work

Store case-study images in `assets/case-studies/`. Reference them from the
body with a site-relative path wrapped in `relative_url` so links survive any
`baseurl` setting:

![Placeholder inline image]({{ "/assets/case-studies/placeholder-inline.svg" | relative_url }})

The hero image at the top of this page comes from the `hero_image` field in
the front matter above — that's the recommended spot for the lead visual.

## The challenge

Describe the client's situation before the engagement: the manual work, the
disconnected tools, the bottleneck that prompted them to reach out.

## What we built

Explain the solution — how the existing tools were mapped, connected, and
automated into a single workflow.

## The outcome

Summarize the impact. The stats in the grid above pull from the `results`
list in the front matter; this section is where you tell the fuller story and
add a client quote.
