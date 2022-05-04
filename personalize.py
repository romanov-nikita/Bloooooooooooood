import math
import opt_parameters as opt
from Q_in import Q_in


def calcParameters(stroke_volume, heart_rate, tsys, p_sys, p_dias, p_out):
    T = 60 / heart_rate
    dt = 0.001
    T = T - (T % dt)
    nmax = int(T // dt)

    Qin_class = Q_in(HR, SV)
    Qin = [Qin_class.Q(i * dt) for i in range(0, nmax + 1)]

    Q_in_avg = sum(Qin) / len(Qin)

    pulse_pressure = p_sys - p_dias
    C = stroke_volume / pulse_pressure

    p_mean = (2 * p_dias + p_sys) / 3
    R2 = (p_mean - p_out) / Q_in_avg
    R1 = opt.optR1(R2, C, stroke_volume, heart_rate, tsys, p_sys, p_dias, p_out)

    parameters = [R1, R2, C]
    return parameters
