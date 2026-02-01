# 📈 Stock Market Dashboard

Dashboard interativo para análise de ações em tempo quase real utilizando
Python, Streamlit, Plotly e Alpha Vantage API.
<img width="1810" height="733" alt="image" src="https://github.com/user-attachments/assets/9d4aff22-6018-403c-92ed-844851bde7ca" />
<img width="1841" height="562" alt="image" src="https://github.com/user-attachments/assets/c8a80c5c-0377-46f2-a084-9e08f39f0d90" />
<img width="1798" height="739" alt="image" src="https://github.com/user-attachments/assets/a0555498-c633-452e-b59d-275ca3220be4" />

##  Funcionalidades

- Gráficos de candlestick interativos
- Indicadores técnicos (SMA, EMA, Bollinger Bands)
- Seleção de múltiplos ativos
- Cache inteligente para reduzir chamadas à API

##  Tecnologias

- Python 3.11
- Streamlit
- Pandas
- Plotly
- Alpha Vantage API
- 
##  Estrutura do Projeto
```text
market_dashboard/
├── services/                    
│   ├── connection.py            # conexão com a API
│   └── market_data.py           # funções de tratamento de dados da API
├── database/ 
│   ├──database_connection.py   # conexão com o banco de dados
│   └── models.py               # criação das tables
├── layout/
│   └──charts.py                # funções de criação dos gráficos
├── app.py
└──requirements.txt             # bibliotecas instaladas
```
##  Como rodar o projeto
```bash
git clone https://github.com/Lipe59XD/Stock_Prices.git
cd Stock_Prices
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
## Variáveis de ambiente (.env)

Muito importante pra API:

```md

Crie um arquivo `.env`:

.env/
API_KEY=''
DATABASE_URL = ""
```
  
