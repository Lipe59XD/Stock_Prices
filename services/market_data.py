from datetime import date
import requests
import pandas as pd
from services.connection import API_KEY, url
import streamlit as st


def fetch_data(url, params):
    response = requests.get(url, params=params)
    data = response.json()
    return data

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

def multiple_normalized_data(selected_symbols):
    normalized_values = pd.DataFrame()
    for k in selected_symbols:
        params = {
            'function': 'TIME_SERIES_DAILY',
            'symbol': k,
            'apikey': API_KEY
        }
        fetched_data = daily_data(k, date.today(), params)
        treated_data = data_treatment(fetched_data)
        normalized = (treated_data['close']/treated_data['close'].iloc[0])*100
        normalized_values[k] = normalized
    return normalized_values

def multiple_volume_data(selected_symbols):
    multiple_volume_data = pd.DataFrame()
    for k in selected_symbols:
        params = {
            'function': 'TIME_SERIES_DAILY',
            'symbol': k,
            'apikey': API_KEY
        }
        fetched_data = daily_data(k, date.today(), params)
        treated_data = data_treatment(fetched_data)
        multiple_volume_data[k] = treated_data['volume']
    return multiple_volume_data
@st.cache_data
def daily_data(symbol, today, params):
    return fetch_data(url, params)