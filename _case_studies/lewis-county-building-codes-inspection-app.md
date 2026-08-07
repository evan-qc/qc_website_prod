---
title: "How Lewis County Building Codes Replaced 24 Spreadsheets with a Custom Inspection Application"
client: "Lewis County Building Codes"
sector: public
rank: 50
capabilities: [automation, dashboards]
summary: "We rebuilt 24 disconnected municipal spreadsheets as a single custom Airtable application - a relational data model, a live inspection dashboard, and automations - so a five-person team can manage fire safety inspections across the county from one place."
description: "How Quantify replaced Lewis County Building Codes' 24 municipal spreadsheets with a custom Airtable inspection application - a relational data model, live dashboard, and automations managing 755 occupancies across 568 properties."

hero_image: "/assets/case-studies/lewis-county-building-codes-inspection-app-hero.jpg"
hero_image_width: 1600
hero_image_height: 1067
hero_image_alt: "A building codes inspector in a high-visibility vest filling out an inspection form on a clipboard over a set of property plans"

results:
  - stat: "24 → 1"
    label: "Municipal spreadsheets replaced by a single relational application"
  - stat: "755"
    label: "Occupancies managed as connected records, across 568 properties"
  - stat: "160+"
    label: "Inspections per year now run through one application and dashboard"
  - stat: "5"
    label: "Inspection officers working in one shared application instead of separate files"
---

Lewis County Building Codes was effectively running a database application inside Excel. Across 24 separate spreadsheets - one per municipality - a five-person team tracked fire safety inspections for 755 occupancies spread over 568 properties. Quantify rebuilt the whole thing as a custom application, giving the team a single source of truth and a live view of what needs attention.

## The challenge

That data was relational, and a spreadsheet is not a relational tool. Each of the 24 sheets held occupancy codes, parcel IDs, inspection statuses, and assigned officers, and the team was creating, reading, updating, and deleting records across all of them by hand.

There was no single source of truth, no way to enforce consistency, and no quick read on completeness or progress. The complexity had simply outgrown what Excel could hold.

## What we built

Quantify began with a thorough discovery process, digging into the subject matter to capture as much of the team's expertise as possible. From that we designed a relational data model and put it through both peer review and client review before building anything. A project charter and clear timeline set the scope and expectations. We built the foundational application, reviewed it with the client, layered automations on top, and reviewed again.

We rebuilt the entire system as a custom application in Airtable, starting with a proper relational data model - properties, occupancies, inspections, municipalities, and officers as connected records instead of 24 disconnected sheets.

![Custom Airtable inspection application showing the properties list grouped by property, with occupancy names, occupancy codes, parcel IDs, and fire safety inspection requirements]({{ "/assets/case-studies/lewis-county-building-codes-inspection-app-01.png" | relative_url }})

On top of that model sits everything spreadsheets could never support:

- **A custom application interface** - one place for the whole team to create, edit, and manage inspections against connected records rather than rows in 24 separate files.
- **A live performance dashboard** - percent overdue, inspections completed per period, and backlog by municipality, with color-coded alerts for expiring and expired inspections.
- **Zapier automations** - notifying property owners about expired inspections and handling the post-inspection save, move, sign, and archive steps that used to be done by hand.
- **A data warehouse connection** - feeding inspection activity into the county's warehouse for consistent, reliable reporting.
- **Virtual training and SOP documentation** - so the five-person team can run and maintain the application with confidence.

*Technical stack: Airtable, Zapier, and the county's Azure data warehouse.*

## The outcome

The team went from 24 disconnected spreadsheets to one custom application built on a real data model. All 755 occupancies now live as connected records in a single system, and the 160-plus inspections the office runs each year flow through one application and dashboard.

**A shared source of truth.** Five inspection officers work in one application instead of separate files, with consistency enforced by the data model rather than by memory.

**Clarity at a glance.** Color-coded alerts and a live dashboard mean the office can immediately see what is overdue, what is expiring, and where the backlog sits by municipality.

**Less manual work.** Automations handle owner notifications and the repetitive save-move-sign-archive steps that used to eat staff time after every inspection.

<figure class="cs-pullquote">
  <blockquote>
    <p>"The live interface and dashboard showing graphics helps this office see and categorize the most urgent projects and needs."</p>
  </blockquote>
  <figcaption>Jonathan Roes<span>Director, Lewis County Building Codes</span></figcaption>
</figure>

<p class="cs-cta" style="margin-top: 2.5rem;"><a class="btn btn-amber" href="mailto:hello@quantify-consulting.com?subject=Interested%20in%20results%20like%20these">Email us</a></p>

Interested in results like these? Let's talk.
