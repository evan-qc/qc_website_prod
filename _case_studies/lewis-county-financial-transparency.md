---
title: "How Lewis County Moved from 5-Day Report Delays to Real-Time Financial Transparency"
client: "Lewis County Government"
sector: public
rank: 10
capabilities: [dashboards]
summary: "We built a cloud analytics layer on top of Lewis County's existing Tyler ERP, turning 3 to 5 day budget reporting into real-time dashboards for staff and the public."
description: "How Quantify gave Lewis County Government real-time financial transparency - connecting its Tyler Munis ERP to an Azure data warehouse and Power BI dashboards for staff and citizens, in three months."

hero_image: "/assets/case-studies/lewis-county-financial-transparency-hero.jpg"
hero_image_width: 1396
hero_image_height: 924
hero_image_alt: "The Lewis County Court House in Lowville, New York"

results:
  - stat: "5 days → real-time"
    label: "Budget report turnaround for department heads"
  - stat: "3 months"
    label: "From kickoff to two live dashboards"
  - stat: "1st"
    label: "Rural upstate NY county with real-time financial transparency"
---

Lewis County Government - a municipal government of 275 employees in Lowville, New York - kept comprehensive financial records in its Tyler Technologies ERP, yet almost no one could actually use them. Between August and October 2025, Quantify built a modern analytics layer on top of that system, turning days-long reporting into real-time visibility for staff and citizens alike.

**[→ View the live public dashboard at lewiscountyny.gov/analytics](https://lewiscountyny.gov/analytics/)**

## The challenge

Lewis County's financial data was trapped. Despite a complete record in the Tyler ERP, only a handful of specialists could pull meaningful information out of it. Department heads waited three to five days for budget reports. County Administrator Tim Hunt had no real-time visibility into spending patterns. And citizens saw how their tax dollars were used only through lengthy annual PDF budget books.

The county wasn't lacking data - it was lacking access and clarity.

## What we built

Quantify built a cloud-based analytics infrastructure that freed the county's financial data from its ERP silo. We connected the Tyler ERP and payroll systems to a centralized Azure SQL data warehouse, with automated ETL pipelines that refresh weekly.

![Data pipeline flowing from Tyler Technologies ERP and SharePoint Excel files through Azure Data Factory and Azure SQL Database into Power BI]({{ "/assets/case-studies/lewis-county-financial-transparency-01.jpg" | relative_url }})

On top of that foundation we delivered two purpose-built dashboards:

- **A public dashboard** at `lewiscountyny.gov/analytics` - real-time county spending, department-by-department trends, and payroll metrics, written in plain language for citizens.
- **An internal dashboard** - everything in the public view, plus line-item detail and drill-down for spotting overspending.

We validated every data point against the county's 2025 published budget book, working closely with County Treasurer Eric Virkler to ensure accuracy. After iterative testing with stakeholders and county legislators, both dashboards launched in October 2025.

*Technical stack: Tyler Munis ERP, SharePoint, Azure Data Factory, Azure SQL Database, and Power BI.*

## The outcome

![Power BI budget dashboard showing 2025 budget versus actual spending, with monthly and cumulative expense trends]({{ "/assets/case-studies/lewis-county-financial-transparency-02.jpg" | relative_url }})

**From days to seconds.** Department heads now access budget data instantly. What used to take three to five days of back-and-forth happens in real time, freeing subject-matter experts from hours of manual report generation.

**Proactive leadership.** Tim Hunt can spot spending trends early and make timely corrections, instead of reacting to problems weeks after they surface.

**Public accountability.** Lewis County became one of the first rural counties in upstate New York to offer real-time financial transparency. Citizens can track tax dollars as they're spent, strengthening public trust.

**A scalable foundation.** The data warehouse made new analytics fast to build - the county has already added a second dashboard for its Solid Waste Department by combining ERP data with transfer-station metrics.

The whole transformation took three months, not three years. The county didn't replace its ERP; it built a modern analytics layer on top of it. Meaningful financial transparency didn't require ripping out legacy systems - just the right architecture and a commitment to turning data into stories stakeholders can act on.

<figure class="cs-pullquote">
  <blockquote>
    <p>"Evan approached the project with a clear vision and structured methodology. He not only met the project objectives but exceeded expectations in terms of quality and impact."</p>
  </blockquote>
  <figcaption>Tim Hunt<span>County Administrator, Lewis County</span></figcaption>
</figure>

**[See it live → lewiscountyny.gov/analytics](https://lewiscountyny.gov/analytics/)**
