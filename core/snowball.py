def snowball_projection(initial_investment, monthly_contrib, years, reinvest=True, annual_return=0.07):
    months = years * 12
    total = initial_investment
    for _ in range(months):
        total = total * (1 + annual_return/12)
        if reinvest:
            total += monthly_contrib
    return total
