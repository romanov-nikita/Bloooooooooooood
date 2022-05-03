import math

# if R1 = 0 --> 2 windk
# if R1 != 0 and L = 0 --> 3 windk
# if R1 != 0 and L != 0 --> 4 windk
def calcPressure(SV, HR, tsys, R1, R2, C, Pout, L):
    T = 60 / HR
    dt = 0.001
    T = T - (T % dt)
    nmax = int(T // dt)
    nsys = int(tsys // dt)
    #print(nmax)
    pi = math.pi

    # initialize input flow and it's first-second derivatives
    Coef = SV * pi / (2 * tsys)
    Qin = [0] * (nmax + 1)
    Qin_der1 = [0] * (nmax + 1)
    Qin_der2 = [0] * (nmax + 1)
    Qin[0:(nsys + 1)] = [Coef * math.sin(pi * dt * i / tsys) for i in range(0, nsys + 1)]
    Qin_der1[0:(nsys + 1)] = [Coef * math.cos(pi * dt * i / tsys) * pi / tsys for i in range(0, nsys + 1)]
    Qin_der2[0:(nsys + 1)] = [-Coef * math.sin(pi * dt * i / tsys) * (pi / tsys)**2 for i  in range (0, nsys + 1)]

    Nc = 10  # number of heart cycles
    P = [0] * (nmax * Nc + 1)

    P[0] = Pout
    for j in range(Nc):
        for i in range(1, nmax + 1):
            Rs = (1 + R1 / R2) * Qin[i] + (C * R1 + L / R2) * Qin_der1[i] + L * C * Qin_der2[i]
            P[i + j * nmax] = R2 * (dt * Rs + P[i - 1 + j * nmax] * C + Pout * dt / R2) / (dt + R2 * C)

    Plast = P[nmax*(Nc-1)+1:nmax * Nc + 2]

    return Plast