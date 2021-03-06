import math
from Q_in import Q_in
import numpy as np

# if R1 = 0 --> 2 windk
# if R1 != 0 and L = 0 --> 3 windk
# if R1 != 0 and L != 0 --> 4 windk
def calcPressure(SV, HR, tsys, R1, R2, C, Pout, L):
    T = 60 / HR
    dt = 0.001
    T = T - (T % dt)
    nmax = int(T // dt)

    # initialize input flow and it's first-second derivatives
    Qin_class = Q_in(HR, SV)
    Qin = [Qin_class.Q(i*dt) for i in range(0, nmax + 1)]
    Qin_der1 = [Qin_class.Q_der1(i*dt) for i in range(0, nmax + 1)]
    Qin_der2 = [Qin_class.Q_der2(i*dt) for i in range (0, nmax + 1)]

    Nc = 10  # number of heart cycles
    P = np.zeros(nmax * Nc + 1)

    P[0] = Pout
    for j in range(Nc):
        for i in range(1, nmax + 1):
            Rs = (1 + R1 / R2) * Qin[i] + (C * R1 + L / R2) * Qin_der1[i] + L * C * Qin_der2[i]
            P[i + j * nmax] = R2 * (dt * Rs + P[i - 1 + j * nmax] * C + Pout * dt / R2) / (dt + R2 * C)

    Plast = P[nmax*(Nc-1)+1:nmax * Nc + 2]

    return np.append(Plast, np.append(Plast, np.append(Plast, np.append(Plast, np.append(Plast, Plast)))))
