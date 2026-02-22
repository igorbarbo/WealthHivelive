import numpy as np

def var_95(returns):
    return np.percentile(returns, 5)
