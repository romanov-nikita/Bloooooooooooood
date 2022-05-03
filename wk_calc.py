import math

def calcPressure(SV, HR, tsys, R, C, Pout):
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
    Qin[0:(nsys + 1)] = [Coef * math.sin(pi * dt * i / tsys) for i in range(0, nsys + 1)]

    Nc = 10  # number of heart cycles
    P = [0] * (nmax * Nc + 1)

    P[0] = Pout
    for j in range(Nc):
        for i in range(1, nmax + 1):
            Rs = Qin[i]
            P[i + j * nmax] = R * (dt * Rs + P[i - 1 + j * nmax] * C + Pout * dt / R) / (dt + R * C)

    Plast = P[nmax*(Nc-1)+1:nmax * Nc + 2]

    return Plast