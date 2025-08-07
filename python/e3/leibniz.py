def leibniz_pi(n_terms):
    pi_estimate = 0
    for k in range(n_terms):
        pi_estimate += (-1) ** k / (2 * k + 1)
    return 4 * pi_estimate


# Example usage
print(leibniz_pi(1000000))  # Higher n_terms → better approximation
