from plotly import graph_objects as go
import plotly.express as px
from services.market_data import data_treatment, daily_data
from datetime import date

def create_candlestick_graph(fetched_data, selected_indicator=None):
    data_frame = data_treatment(fetched_data)
    candlestick_graph = go.Figure(data=[
        go.Candlestick(
            x = data_frame.index,
            open = data_frame['open'],
            high = data_frame['high'],
            low = data_frame['low'],
            close = data_frame['close']
        )
    ])
    candlestick_graph.update_layout(
        yaxis_title='Price (USD per Share)',
        xaxis_title='Date'
    )
    data_frame['SMA20'] = data_frame['close'].rolling(20).mean()
    data_frame['EMA20'] = data_frame['close'].ewm(20).mean()
    data_frame['BB_STD'] = data_frame['close'].rolling(20).std()
    data_frame['BB_UPPER'] = data_frame['SMA20'] + (data_frame['BB_STD'] * 2)
    data_frame['BB_LOWER'] = data_frame['SMA20'] - (data_frame['BB_STD'] * 2)
    if "SMA20" in selected_indicator:
        candlestick_graph.add_trace(
            go.Scatter(
                x=data_frame.index,
                y=data_frame['SMA20'],
                mode='lines',
                name='SMA20'
            )
        )
    if "EMA20" in selected_indicator:
        candlestick_graph.add_trace(
            go.Scatter(
                x=data_frame.index,
                y=data_frame['EMA20'],
                mode='lines',
                name='EMA20'
            )
        )
    if "BOLLINGER BANDS" in selected_indicator:
        candlestick_graph.add_trace(
            go.Scatter(
                x=data_frame.index,
                y=data_frame['BB_UPPER'],
                line=dict(color='rgba(173,216,230,0.5)'),
                name='BB Upper',
                showlegend=True
            )
        )
        candlestick_graph.add_trace(
            go.Scatter(
                x=data_frame.index,
                y=data_frame['BB_LOWER'],
                line=dict(color='rgba(173,216,230,0.5)'),
                name='BB Lower',
                fill='tonexty',
                fillcolor='rgba(173,216,230,0.2)',
                showlegend=True
            )
        )
    return candlestick_graph


def create_volume_line_graph(multiple_volume_data, selected_symbols):
     df = multiple_volume_data.copy()
     df["Date"] = df.index
     line_graph = px.line(
        df,
        x= "Date",
        y= selected_symbols,
        title="Stock Volume Over Time"
    )
     line_graph.update_layout(
        yaxis_title='Volume',
        xaxis_title='Date',
        legend_title='Stock Symbols'
    )
     return line_graph

def create_normalized_line_graph(multiple_normalized_data, selected_symbols, selected_indicators=None):
    fig = px.line(
        multiple_normalized_data,
        x=multiple_normalized_data.index,
        y=selected_symbols,
        title="Normalized Stock Prices Over Time"
    )
    fig.update_layout(
        yaxis_title='Normalized Price (%)',
        xaxis_title='Date',
        legend_title='Stock Symbols'
    )
    return fig

