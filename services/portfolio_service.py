from database.crud import create_portfolio, add_asset_to_portfolio
from core.optimizer import Optimizer
import pandas as pd

def create_new_portfolio(client_id, name, assets_dict):
    """
    assets_dict: {'TICKER': quantity}
    """
    portfolio = create_portfolio(client_id, name)
    for ticker, qty in assets_dict.items():
        add_asset_to_portfolio(portfolio.id, ticker, qty)
    return portfolio

def optimize_portfolio_weights(prices_df):
    """
    Retorna pesos ótimos via Sharpe ratio
    """
    returns = prices_df.pct_change().dropna()
    cov = returns.cov()
    weights = Optimizer.maximize_sharpe(returns, cov)
    return weights
