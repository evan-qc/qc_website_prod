---
title: "How Lewis County Solid Waste Transformed Disconnected Data Systems Into Strategic Operations Intelligence"
client: "Lewis County Solid Waste Department"
sector: public
summary: "We unified the Solid Waste Department's scale system, ERP, and Excel records into one Azure data warehouse powering real-time public and internal dashboards."
description: "How Lewis County Solid Waste connected its Compu-Weigh scale data, Tyler Munis ERP, and Excel records into a single Azure SQL warehouse with Power BI dashboards for strategic decision-making and public transparency."
hero_image: "/assets/case-studies/lewis-county-solid-waste-operations-intelligence-hero.jpg"
hero_image_alt: "A waste-collection truck unloading at a transfer station"
results:
  - stat: "3 → 1"
    label: "Disconnected systems unified into one Azure data warehouse"
  - stat: "2"
    label: "Transfer stations with real-time performance visibility"
  - stat: "2"
    label: "Strategic dashboards — one public, one internal"
---

Lewis County's two transfer stations process thousands of tons of waste and recyclables every year — and the data behind those operations lived in three systems that never spoke to each other. We built the intelligence layer that connects them, turning scattered records into real-time strategic insight for leadership and the public alike.

## The challenge

Department Director Kip Turck and his team tracked critical metrics like diversion rates and gross margins, but the data needed to make informed operational decisions was scattered across incompatible systems. The Compu-Weigh scale system logged tonnage data on a Paradigm server. The Tyler Munis ERP tracked department budgets and spending. Principal Account Clerk Denise Yost maintained detailed operational records in Excel spreadsheets. None of these systems communicated with each other.

When County Administrator Tim Hunt needed to evaluate tip fee structures, vehicle maintenance costs, or staffing capacity, there was no unified view of how financial spending correlated with waste volumes. The department had comprehensive data — it just didn't tell a coherent story.

## What we built

Building on the foundation established by our county-wide financial transparency project, we integrated the department's fragmented data systems into a strategic operations platform.

![Data flow from the Compu-Weigh scale system, Tyler Munis ERP, and Excel into the Azure SQL data warehouse, feeding Power BI dashboards and reports]({{ "/assets/case-studies/lewis-county-solid-waste-operations-intelligence-01.png" | relative_url }})

**Centralized data warehouse.** We connected the Compu-Weigh Paradigm server, Tyler Munis ERP, and Excel-tracked operational data into the existing Azure SQL data warehouse, creating automated pipelines that unify financial and operational metrics.

**Data standardization and cleaning.** Raw tonnage data, budget line items, and operational records were cleaned, standardized, and organized around the strategic KPIs leadership actually uses for decision-making.

**Two strategic dashboards.** A public dashboard shares real-time data with citizens, demonstrating the department's stewardship. An internal dashboard adds financial cost analysis, cross-station comparisons, and detailed expense tracking for vehicle maintenance and operations.

![Power BI dashboard showing month-over-month net tons by material type across Lewis County's transfer stations]({{ "/assets/case-studies/lewis-county-solid-waste-operations-intelligence-02.jpg" | relative_url }})

We re-architected the existing Power BI infrastructure around high-level strategic metrics rather than raw data dumps: real-time **diversion rate** tracking of waste diverted from landfills, **YTD recycling volume** measured against the 3,000-ton OHSWA threshold, and **cost-per-ton analysis** across both transfer stations.

**Technical stack:** Compu-Weigh Paradigm Server, Tyler Munis ERP, Excel integration, Azure Data Factory, Azure SQL Database, Power BI.

## The outcome

**Strategic decision-making.** Leadership can now correlate spending with waste volumes, enabling data-driven decisions on tip fees, vehicle replacement, and staffing.

**Operational efficiency.** Real-time performance metrics across both transfer stations reveal efficiency opportunities and bottlenecks instantly.

**Public accountability.** Residents see real-time environmental impact metrics, demonstrating responsible waste management.

Lewis County Solid Waste connected existing systems rather than replacing them — the Compu-Weigh scales, Tyler ERP, and Excel spreadsheets all remained in place. Because the project leveraged infrastructure from our county-wide financial transparency initiative, development moved quickly without rebuilding integration pipelines: a demonstration of how strategic data architecture delivers compounding returns.

[View the live dashboard on the Lewis County website](https://lewiscountyny.gov/departments/solid-waste/#analytics)
