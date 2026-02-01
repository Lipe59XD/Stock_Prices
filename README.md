# 📈 Stock Market Dashboard

Interactive dashboard for near real-time stock market analysis built with  
Python, Streamlit, Plotly, and the Alpha Vantage API.

<img width="1810" height="733" alt="Dashboard overview" src="https://github.com/user-attachments/assets/9d4aff22-6018-403c-92ed-844851bde7ca" />
<img width="1841" height="562" alt="Candlestick chart" src="https://github.com/user-attachments/assets/c8a80c5c-0377-46f2-a084-9e08f39f0d90" />
<img width="1798" height="739" alt="Technical indicators" src="https://github.com/user-attachments/assets/a0555498-c633-452e-b59d-275ca3220be4" />

---

## Features

- Interactive candlestick charts
- Technical indicators (SMA, EMA, Bollinger Bands)
- Multiple asset selection
- Smart caching to reduce API calls

---

## Technologies

- Python 3.11
- Streamlit
- Pandas
- Plotly
- Alpha Vantage API

## Project Structure

```text
market_dashboard/
├── services/
│   ├── connection.py             # API connection
│   └── market_data.py            # API data fetching and processing
├── database/
│   ├── database_connection.py    # Database connection
│   └── models.py                 # Table models
├── layout/
│   └── charts.py                 # Chart creation functions
├── app.py                        # Main Streamlit application
└── requirements.txt              # Project dependencies
```
## How to Run the Project
```bash
git clone https://github.com/Lipe59XD/Stock_Prices.git
cd Stock_Prices
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Environment variables (.env)

```md
## 🔐 Environment variables

create a file  `.env`:

.env/
API_KEY=''
DATABASE_URL = ""
```
