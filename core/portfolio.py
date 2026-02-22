import pandas as pd
import numpy as np

class Portfolio:
    def __init__(self, assets, prices):
        self.assets = assets
        self.prices = prices  # DataFrame: cada coluna um ativo

    def returns(self):
        return self.prices.pct_change().dropna()

    def portfolio_return(self, weights):
        returns = self.returns()
        return np.sum(returns.mean() * weights) * 252

    def portfolio_volatility(self, weights):
        returns = self.returns()
        return np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
