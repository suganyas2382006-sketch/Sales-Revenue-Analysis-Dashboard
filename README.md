# 📊 Sales & Revenue Analysis Dashboard

## Project Overview
The Sales & Revenue Analysis Dashboard is an interactive data visualization project developed using Python, Streamlit, Pandas, and Plotly. The dashboard helps analyze sales performance, revenue trends, top-performing products, and regional business insights through visual charts and KPI metrics.

## Objectives
- Analyze sales and revenue data
- Track important KPI metrics
- Generate business insights
- Provide interactive filtering and visualization

## Features

### Data Import
- Import data from CSV files
- Support for Excel files (.xlsx)

### KPI Metrics
- Total Sales
- Total Revenue
- Average Units Sold

### Interactive Visualizations
- Revenue Trend Line Chart
- Top Performing Products Bar Chart
- Revenue by Category Pie Chart
- Region-wise Revenue Analysis

### Filters / Slicers
- Product Filter
- Region Filter
- Category Filter

## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- OpenPyXL

## Dataset Structure

| Column | Description |
|----------|-------------|
| Order_ID | Unique order ID |
| Date | Transaction date |
| Product | Product name |
| Category | Product category |
| Region | Sales region |
| Sales | Units sold |
| Unit_Price | Price per unit |
| Revenue | Total revenue |

Date format used:

```text
%m %d %y
Example:
01 15 25
```

## Project Structure

```text
Sales-Revenue-Analysis-Dashboard/
│
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── sales_data.csv
```

## Installation

Install required libraries:

```bash
pip install streamlit pandas plotly openpyxl
```

## Run Project

```bash
python -m streamlit run app.py
```

or

```bash
python3 -m streamlit run app.py
```

## Dashboard Output

The dashboard displays:

- KPI cards
- Revenue trend analysis
- Top product analysis
- Category-wise revenue distribution
- Region-wise performance analysis

## Business Insights

- Tablet generated the highest revenue.
- Electronics category contributed most revenue.
- East region showed the highest revenue.
- Total revenue generated: ₹13,030
- Total sales achieved: 68 units.
- Revenue spikes observed during mid-January.

## Expected Outcome

This project helps in learning:

- Data visualization
- KPI tracking
- Business insight generation
- Interactive dashboard development

## Author

Submitted by: Suganya S