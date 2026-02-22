def rebalance(weights, target_weights):
    diff = target_weights - weights
    return weights + diff * 0.5  # exemplo simples de rebalanceamento parcial
