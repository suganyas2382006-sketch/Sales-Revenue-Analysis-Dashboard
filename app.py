import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Sales Dashboard",
                   layout="wide")

st.title("📊 Sales & Revenue Analysis Dashboard")

# Upload option
uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

df = None

# If uploaded file exists
if uploaded_file is not None:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

# Otherwise load default file from folder
elif os.path.exists("data/sales_data.csv"):
    df = pd.read_csv("data/sales_data.csv")
    st.success("Loaded default dataset")

if df is not None:

    st.write("### Dataset Preview")
    st.dataframe(df.head())

    df['Date'] = pd.to_datetime(df['Date'])

    total_sales = df['Sales'].sum()
    total_revenue = df['Revenue'].sum()
    avg_sales = df['Sales'].mean()

    c1, c2, c3 = st.columns(3)

    c1.metric("Total Sales", total_sales)
    c2.metric("Revenue", f"₹{total_revenue:,.0f}")
    c3.metric("Average Sales", round(avg_sales,2))

    trend = (
        df.groupby('Date')['Revenue']
        .sum()
        .reset_index()
    )

    fig1 = px.line(
        trend,
        x='Date',
        y='Revenue',
        title='Revenue Trend'
    )

    st.plotly_chart(fig1, use_container_width=True)

    top = (
        df.groupby('Product')['Revenue']
        .sum()
        .reset_index()
    )

    fig2 = px.bar(
        top,
        x='Product',
        y='Revenue',
        title='Top Products'
    )

    st.plotly_chart(fig2, use_container_width=True)

else:
    st.warning("No dataset found")