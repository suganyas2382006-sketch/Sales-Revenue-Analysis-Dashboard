import streamlit as st
import pandas as pd
import plotly.express as px

# Page setup
st.set_page_config(page_title="Sales & Revenue Dashboard",
                   layout="wide")

st.title("📊 Sales & Revenue Analysis Dashboard")

# Upload file
uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

if uploaded_file:

    # Read file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    else:
        df = pd.read_excel(uploaded_file)

    st.write("### Dataset Preview")
    st.dataframe(df.head())

    # Convert date column
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])

    # Sidebar Filters
    st.sidebar.header("Filters")

    if 'Product' in df.columns:
        products = st.sidebar.multiselect(
            "Select Product",
            df['Product'].unique(),
            default=df['Product'].unique()
        )

        df = df[df['Product'].isin(products)]

    if 'Region' in df.columns:
        regions = st.sidebar.multiselect(
            "Select Region",
            df['Region'].unique(),
            default=df['Region'].unique()
        )

        df = df[df['Region'].isin(regions)]

    # KPIs
    total_sales = df['Sales'].sum()
    total_revenue = df['Revenue'].sum()
    avg_sales = df['Sales'].mean()

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Sales", f"{total_sales:,.0f}")
    col2.metric("Total Revenue", f"₹{total_revenue:,.0f}")
    col3.metric("Average Sales", f"{avg_sales:.2f}")

    st.markdown("---")

    # Revenue Trend
    if 'Date' in df.columns:

        trend = df.groupby('Date')['Revenue'].sum().reset_index()

        fig1 = px.line(
            trend,
            x='Date',
            y='Revenue',
            title='Revenue Trend'
        )

        st.plotly_chart(fig1, use_container_width=True)

    # Top Products
    top_products = (
        df.groupby('Product')['Revenue']
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig2 = px.bar(
        top_products,
        x='Product',
        y='Revenue',
        title='Top Performing Products'
    )

    st.plotly_chart(fig2,
                    use_container_width=True)

    # Region Sales
    if 'Region' in df.columns:

        region_sales = (
            df.groupby('Region')['Sales']
            .sum()
            .reset_index()
        )

        fig3 = px.pie(
            region_sales,
            names='Region',
            values='Sales',
            title='Sales by Region'
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

else:
    st.info("Upload a CSV or Excel file to start.")