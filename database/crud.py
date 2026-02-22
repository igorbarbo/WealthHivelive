from database.connection import SessionLocal
from database.models import Client, Portfolio, Asset

def create_client(name, age):
    session = SessionLocal()
    client = Client(name=name, age=age)
    session.add(client)
    session.commit()
    session.refresh(client)
    session.close()
    return client

def create_portfolio(client_id, name):
    session = SessionLocal()
    portfolio = Portfolio(name=name, client_id=client_id)
    session.add(portfolio)
    session.commit()
    session.refresh(portfolio)
    session.close()
    return portfolio

def add_asset_to_portfolio(portfolio_id, ticker, quantity):
    session = SessionLocal()
    asset = Asset(ticker=ticker, quantity=quantity, portfolio_id=portfolio_id)
    session.add(asset)
    session.commit()
    session.refresh(asset)
    session.close()
    return asset

def get_client_portfolios(client_id):
    session = SessionLocal()
    portfolios = session.query(Portfolio).filter(Portfolio.client_id==client_id).all()
    session.close()
    return portfolios
