import numpy as np

def monte_carlo_simulation(prices, initial_investment=10000, periods=252, simulations=1000):
    returns = prices.pct_change().dropna()
    mean = returns.mean()
    cov = returns.cov()
    results = []
    for _ in range(simulations):
        simulated = np.random.multivariate_normal(mean, cov, periods)
        cumulative = (simulated + 1).cumprod() * initial_investment
        results.append(cumulative[-1])
    return results
