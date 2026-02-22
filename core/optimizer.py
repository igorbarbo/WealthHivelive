import numpy as np
from scipy.optimize import minimize

class Optimizer:
    @staticmethod
    def maximize_sharpe(returns, cov):
        n = len(returns.columns)
        def neg_sharpe(weights):
            port_return = np.sum(returns.mean() * weights) * 252
            port_vol = np.sqrt(np.dot(weights.T, np.dot(cov*252, weights)))
            return -port_return / port_vol
        constraints = ({'type':'eq', 'fun': lambda w: np.sum(w)-1})
        bounds = [(0,1) for _ in range(n)]
        res = minimize(neg_sharpe, n*[1./n,], bounds=bounds, constraints=constraints)
        return res.x
