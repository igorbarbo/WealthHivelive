import yfinance as yf
import pandas as pd

def get_stock_data(ticker, start="2016-01-01", end="2026-01-01"):
    """
    Retorna histórico diário de preços de um ticker do Yahoo Finance
    """
    df = yf.download(ticker, start=start, end=end)
    df = df[['Open','High','Low','Close','Adj Close','Volume']]
    df.dropna(inplace=True)
    return df
