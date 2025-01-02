import streamlit as st
import pandas as pd
import plotly.express as px


historical_data = pd.read_csv('historical_demand_trends.csv')
forecasted_data = pd.read_csv('forecasted_demand.csv')
safety_stock_data = pd.read_csv('safety_stock_levels.csv')

# Streamlit dashboard layout
st.title("Inventory Optimization Dashboard")


st.header("1. Historical Demand Trends")
region = st.selectbox("Select Region", historical_data['Region'].unique())
filtered_historical = historical_data[historical_data['Region'] == region]
fig1 = px.line(filtered_historical, x='Sales_Date', y='Quantity_Sold', title=f'Historical Demand Trends - {region}')
st.plotly_chart(fig1)


st.header("2. Forecasted Demand by Region and Product Category")
forecast_region = st.selectbox("Select Forecast Region", forecasted_data['Region'].unique())
forecast_category = st.selectbox("Select Product Category", forecasted_data['Category'].unique())
filtered_forecast = forecasted_data[
    (forecasted_data['Region'] == forecast_region) &
    (forecasted_data['Category'] == forecast_category)
]
fig2 = px.line(filtered_forecast, x='ds', y='yhat', title=f'Forecasted Demand - {forecast_region} - {forecast_category}')
st.plotly_chart(fig2)


st.header("3. Safety Stock Levels for Top 10 Volatile Products")
fig3 = px.bar(safety_stock_data, x='Product_ID', y='safety_stock', title="Safety Stock Levels")
st.plotly_chart(fig3)
i
