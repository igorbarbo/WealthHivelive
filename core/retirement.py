def retirement_projection(current_savings, monthly_contrib, years, annual_return=0.07):
    months = years * 12
    total = current_savings
    for _ in range(months):
        total = total * (1 + annual_return/12) + monthly_contrib
    return total
