from sympy import Piecewise

def compress_piecewise(G, t_symbol, dt):
    """
    Parameters:
        G: list or array
        t_symbol: sympy symbol (e.g. F.t)
        dt: timestep width

    Returns:
        sympy Piecewise expression
    """
    conditions = []

    start_index = 1
    current_val = G[0]

    for i in range(1, len(G)):
        if G[i] != current_val:
            t_min = dt * start_index
            t_max = dt * (i + 1)
            condition = (t_symbol >= t_min) & (t_symbol < t_max)
            conditions.append((float(current_val), condition))
            current_val = G[i]
            start_index = i + 1

    t_min = dt * start_index
    t_max = dt * (len(G) + 1)
    condition = (t_symbol >= t_min) & (t_symbol < t_max)
    conditions.append((float(current_val), condition))

    conditions.append((0.0, True))
    return Piecewise(*conditions)
