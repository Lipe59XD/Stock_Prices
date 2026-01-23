import streamlit as st
import plotly.graph_objects as go
from connection import API_KEY, url
import pandas as pd
import requests

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

st.title("Stock Data Visualization")
#Select stock symbol
symbol = st.selectbox("Select Stock Symbol", options=["IBM", "AAPL", "GOOGL", "MSFT"], index=0)
params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': symbol,
    'interval': '5min',
    'apikey': API_KEY
}
data = requests.get(url, params=params).json()
# Error handling for API response
if "Error Message" in data:
    raise ValueError("Error in API call:", data["Error Message"])
if "Note" in data:
    raise RuntimeError("API call limit reached:", data["Note"])
if not data:
    raise ValueError("No data returned from API.")
else:
    print("Data fetched successfully.")

graph = go.Figure(data=[
    go.Candlestick(
        x = data_treatment(data).index,
        open = data_treatment(data)['open'],
        high = data_treatment(data)['high'],
        low = data_treatment(data)['low'],
        close = data_treatment(data)['close']
    )
    ])
graph.update_layout(
    yaxis_title='Price (USD per Share)',
    xaxis_title='Date'
)
st.header(f"{symbol} Daily Candlestick Chart")
st.plotly_chart(graph, use_container_width=True)
print(symbol)
st.header(f"{symbol} Daily Trading Volume")
st.line_chart(data_treatment(data)[['volume']])

