# 🛒 E-Commerce Sales Analytics Dashboard
### SQL • Python • Power BI • ETL • Data Visualization

![Dashboard](screenshots/dashboard.png)

---

## 📌 Project Overview

An end-to-end data analytics project analysing **100,000+ real e-commerce orders** from the Olist Brazilian E-Commerce dataset. This project covers the complete Data Analyst workflow — raw data ingestion, SQL analysis, Python ETL pipeline, and interactive Power BI dashboard — uncovering actionable business insights across revenue, customer behaviour, product performance, and logistics.

---

## 🎯 Business Questions Answered

| # | Business Question | Insight Found |
|---|---|---|
| 1 | How did revenue trend over time? | Revenue grew **12x in 7 months** (Oct 2016 → May 2017) |
| 2 | Which product categories drive the most revenue? | Beauty & Health (beleza_saude) leads at **R$1.26M** |
| 3 | Which states have the highest average order value? | PB (Paraíba) leads at **R$248 avg order value** |
| 4 | How has the cancellation rate changed over time? | Dropped from **7.4% (2016) to under 1.5% (2017+)** |
| 5 | What is the customer retention rate? | Only **3.12% repeat buyers** — critical retention problem |
| 6 | Does delivery time affect customer satisfaction? | **1-star orders take 2x longer** (20.8 days vs 10.2 days) |
| 7 | Which payment methods drive the most revenue? | Credit card dominates at **R$12.54M (77% of revenue)** |
| 8 | What are the top revenue months? | **November 2017** (Black Friday) = highest at R$1.19M |

---

## 🔑 Key Insights

> **Delivery time is the #1 driver of customer satisfaction.**
> Orders delivered within 10 days average 5-star reviews. Orders taking 20+ days average 1-star reviews — a 50% drop in satisfaction.

> **96.88% of customers never return.**
> The business has a severe retention problem — nearly all revenue depends on acquiring new customers rather than retaining existing ones.

> **Beauty & Health is the star category.**
> beleza_saude generates R$1.26M — 27% more than the second highest category.

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| **SQL (SQLite)** | Data extraction, transformation, business queries |
| **Python (Pandas)** | ETL pipeline, CSV export automation |
| **Power BI** | Interactive dashboard, DAX measures, data modelling |
| **GitHub** | Version control and portfolio hosting |

---

## 📁 Project Structure

```
ecommerce-sales-analytics/
│
├── README.md
│
├── sql/
│   └── queries.sql              # All 8 business SQL queries
│
├── python/
│   └── export.py                # ETL pipeline — loads CSVs, runs queries, exports results
│
├── dashboard/
│   └── ecommerce_sales_dashboard.pbix   # Power BI dashboard file
│
├── data/
│   └── monthly_revenue.csv
│   └── top_categories.csv
│   └── revenue_by_state.csv
│   └── cancellation_rate.csv
│   └── customer_retention.csv
│   └── delivery_vs_reviews.csv
│   └── payment_types.csv
│   └── top_revenue_months.csv
│
└── screenshots/
    └── dashboard.png            # Full dashboard screenshot
```

---

## 📊 Dashboard Visuals

| Visual | Type | Insight |
|---|---|---|
| Monthly Revenue Trend | Line Chart | 12x revenue growth from 2016 to 2018 |
| Top 10 Product Categories | Bar Chart | Beauty & Health dominates |
| Order Cancellation Rate | Area Chart | Dramatic improvement from 7.4% to under 1% |
| Repeat vs One-Time Buyers | Donut Chart | 96.88% one-time buyers — retention crisis |
| Delivery Days vs Review Score | Column Chart | Slower delivery = lower ratings |
| Revenue by Payment Type | Treemap | Credit card = 77% of all revenue |

**Slicers:** Filter by Month • Filter by Category • Filter by Payment Type

---

## 🗃️ Dataset

- **Source:** [Olist Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) — Kaggle
- **Size:** 100,000+ orders across 9 tables
- **Period:** September 2016 — October 2018
- **Tables used:** olist_orders, olist_order_items, olist_products, olist_customers, olist_order_payments, olist_order_reviews

---

## ▶️ How to Run

1. Download the Olist dataset from Kaggle
2. Place all CSV files in the project folder
3. Run `python/export.py` to generate all 8 analysis CSV files
4. Open `dashboard/ecommerce_sales_dashboard.pbix` in Power BI Desktop
5. Refresh data source to point to your local CSV files

---

## 👩‍💻 Author

**Rekhasree Kadirimangalam**
Data Analyst | SQL • Power BI • Python • Excel
[LinkedIn](https://www.linkedin.com/in/kadirimangalam-rekhasree-3434a71a0)
