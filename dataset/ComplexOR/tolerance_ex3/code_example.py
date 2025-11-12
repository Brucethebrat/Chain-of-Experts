def tolerance_ex3(k, t_min, T_max):
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
    num_components = len(k)
    total_cost, tolerances = 0, list(np.zeros(num_components))
    return total_cost, tolerances