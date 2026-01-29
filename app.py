import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from services.connection import API_KEY, url
import pandas as pd
import requests
from datetime import date
from services.market_data import fetch_data, data_treatment, daily_data, multiple_normalized_data, multiple_volume_data
from layout.charts import create_candlestick_graph, create_volume_line_graph, create_normalized_line_graph

st.set_page_config(
    page_title="Stock Market Data Visualization",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.header("Stock Market Data Visualization")
"""
    Choose a stock symbol and chart types to visualize the stock market data.
"""
""
collum1, collum2 = st.columns([1, 5])


# Select Chart Types
with collum1.container(border=True):
    st.write("##### Select Chart Types") 
    chart_types = st.multiselect("", ["Candlestick Chart", "Normalized Line Chart"])

# Select Stock Symbol
with collum1.container(border=True):
    st.write("##### Select Stock Symbol")

    options = ["AAPL", "IBM", "GOOGL", "MSFT", "NVDA", "AMZN", "TSLA", "META"]
    selected = []
    for option in options:
        if st.checkbox(option):
            selected.append(option)


# Display Volume Chart
with collum2.container(border=True):
    st.subheader("Volume Over Time", text_alignment="center")
    st.plotly_chart(create_volume_line_graph(multiple_volume_data(selected), selected))

# Display Normalized Line Chart
if "Normalized Line Chart" in chart_types:
    with st.container(border=True):
        if len(selected) > 1:
            st.subheader("Normalized Line Chart", text_alignment="center")
            st.plotly_chart(create_normalized_line_graph(multiple_normalized_data(selected), selected))
        else:
            st.warning("Please select at least two stock symbols for Normalized Line Chart.")


collum3, collum4 = st.columns([1, 5])
if "Candlestick Chart" in chart_types:
    with collum3.container(border=True):
        st.write("##### Select Stock Symbol for Candlestick Chart")
        symbol = st.radio("", options=["AAPL", "IBM", "GOOGL", "MSFT", "NVDA", "AMZN", "TSLA", "META"])
        params = {
            'function': 'TIME_SERIES_DAILY',
            'symbol': symbol,
            'apikey': API_KEY
        }
    daily_data = daily_data(symbol, date.today(), params)
    with collum3.container(border=True):
        indicator_options = ["SMA20", "EMA20", "BOLLINGER BANDS"]
        indicator_selected = []
        st.write("##### Select Tecnical Indicator")
        for indicator in indicator_options:
            if st.checkbox(indicator):
                indicator_selected.append(indicator)

# Display Candlestick Chart
    with collum4.container(border=True):
        st.subheader(f"{symbol} Candlestick Chart", text_alignment="center")
        st.plotly_chart(create_candlestick_graph(daily_data, indicator_selected))
    # Display Raw Data
    with st.expander("Raw_Data"):
        st.write(data_treatment(daily_data))



