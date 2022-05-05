import wk_calc


# find x_opt (R1 = R2 / x_opt) such as max(P)~p_sys and min(P)~p_dias and return R1
def optR1(R2, C, stroke_volume, heart_rate, tsys, p_sys, p_dias, p_out):
    delta_opt = 0.1
    for x in range(7, 25):
        R1 = R2 / x
        P = wk_calc.calcPressure(stroke_volume, heart_rate, tsys, R1, R2, C, p_out, 0.0)
        delta = max((abs(max(P) - p_sys)) / p_sys, (abs(min(P) - p_dias)) / p_dias)
        if delta < delta_opt:
            x_opt = x
            delta_opt = delta
    return R2 / x_opt


