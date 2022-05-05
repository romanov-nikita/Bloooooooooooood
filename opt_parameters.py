import wk_calc


def optR1(R2, C, stroke_volume, heart_rate, tsys, p_sys, p_dias, p_out):
    delta_opt = 100
    for x in range(10, 40, 5):
        R1 = 2 * R2 / x
        P = wk_calc.calcPressure(stroke_volume, heart_rate, tsys, R1, R2, C, p_out, 0.0)
        delta = max(abs(max(P) - p_sys), abs(min(P) - p_dias))
        if delta < delta_opt:
            x_opt = x / 2
            delta_opt = delta
    return R2 / x_opt
