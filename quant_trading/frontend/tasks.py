# from quant_trading import celery_app
import yfinance as yf
# data = yf.download("AAPL", start="2020-01-01", end="2021-01-01")

# @celery_app.task
# def fetch_data()
# data = yf.download("AAPL", period="5d")
data = yf.Ticker("MSFT")
print(data.insider_transactions)