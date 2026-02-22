from core.montecarlo import monte_carlo_simulation
from core.retirement import retirement_projection
from core.snowball import snowball_projection

def monte_carlo_portfolio(prices, initial_investment=10000, periods=252, simulations=1000):
    return monte_carlo_simulation(prices, initial_investment, periods, simulations)

def simulate_retirement(current_savings, monthly_contrib, years, annual_return=0.07):
    return retirement_projection(current_savings, monthly_contrib, years, annual_return)

def simulate_snowball(initial_investment, monthly_contrib, years, reinvest=True, annual_return=0.07):
    return snowball_projection(initial_investment, monthly_contrib, years, reinvest, annual_return)
