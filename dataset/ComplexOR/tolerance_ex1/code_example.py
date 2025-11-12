def tolerance_ex1(k, t_min, T_max):
    """
    Args:
        "k": cost coefficients
        "t_min": minimum allowable tolerance
        "T_max": total assembly tolerance constraint
    
    Returns:
        "tolerances": the optimal tolerances found
        "total_cost": the minimized cost
    """
    import numpy as np
    num_components = len(k)
    total_cost, tolerances = 0, list(np.zeros(num_components))
    return total_cost, tolerances