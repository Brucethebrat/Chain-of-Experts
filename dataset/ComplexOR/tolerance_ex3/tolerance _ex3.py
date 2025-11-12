def tolerance_ex3(k, t_min, T_max, alpha, beta):
    """
    Args:
        "k": Cost coefficients for components A, B, and C
        "t_min": Minimum manufacturable tolerance
        "T_max": Maximum allowable RSS stack-up
        "alpha": Weight for cost in objective
        "beta": Weight for quality penalty in objective
        
    Returns:
        "tolerances": the optimal tolerances found
        "total_cost": the minimized cost
    """
    import numpy as np
    from scipy.optimize import minimize
    # num_components = len(k)
    # total_cost, tolerances = 0, list(np.zeros(num_components))
    k_arr = np.array(k)

    def total_objective(t):
        cost = np.sum(k_arr / t**2)
        quality_penalty = np.sum(t)
        return alpha * cost + beta * quality_penalty

    def rss_constraint(t):
        return T_max - np.sqrt(np.sum(t**2))

    bounds = [(t_min, None)] * len(k)
    x0 = np.array([0.1] * len(k))
    constraints = [{'type': 'ineq', 'fun': rss_constraint}]
    
    result = minimize(total_objective, x0, method='SLSQP', bounds=bounds, constraints=constraints)
    
    return result.fun
    #     "output": {
    #         "tolerances": result.x.tolist(),
    #         "total_objective": result.fun
    #     }
    # }