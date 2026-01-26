import streamlit as st
import plotly.graph_objects as go
from connection import API_KEY, url
import pandas as pd
import requests
from datetime import date


#Select stock symbol
symbol = st.selectbox("Select Stock Symbol", options=["IBM", "AAPL", "GOOGL", "MSFT"], index=0)
params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': symbol,
    'interval': '5min',
    'apikey': API_KEY
}

# Fetch data from API
def fetch_data(url, params):
    response = requests.get(url, params=params)
    data = response.json()
    return data

# Function to process the data
def data_treatment(data):
    serie = data['Time Series (Daily)']
    data_frame = pd.DataFrame.from_dict(serie, orient='index')
    data_frame = data_frame.rename(columns={
        '1. open': 'open',
        '2. high': 'high',
        '3. low': 'low',
        '4. close': 'close',
        '5. volume': 'volume'})
    data_frame.index = pd.to_datetime(data_frame.index)
    data_frame = data_frame.astype(float)
    data_frame = data_frame.sort_index()
    return data_frame

# Caching the data to optimize performance
@st.cache_data
def daily_data(symbol, today):
    return fetch_data(url, params)


# Main Streamlit App
st.title("Stock Data Visualization")
graph = go.Figure(data=[
    go.Candlestick(
        x = data_treatment(daily_data(symbol, date.today())).index,
        open = data_treatment(daily_data(symbol, date.today()))['open'],
        high = data_treatment(daily_data(symbol, date.today()))['high'],
        low = data_treatment(daily_data(symbol, date.today()))['low'],
        close = data_treatment(daily_data(symbol, date.today()))['close']
    )
    ])
graph.update_layout(
    yaxis_title='Price (USD per Share)',
    xaxis_title='Date'
)
st.header(f"{symbol} Daily Candlestick Chart")
st.plotly_chart(graph, use_container_width=True)

st.header(f"{symbol} Daily Trading Volume")
st.line_chart(data_treatment(daily_data(symbol, date.today()))[['volume']])

