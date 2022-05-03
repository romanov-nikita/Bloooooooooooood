
import matplotlib.pyplot as plt
import wk_calc


def main():
    print("Start")
    SV = 70
    HR = 65
    tsys = 0.33
    R = 0.7
    C = 2.196
    Pout = 35
    P = wk_calc.calcPressure(SV, HR, tsys, 0.07, R, C, Pout, 0.0)
    Psys = max(P)
    Pdia = min(P)
    plt.plot(P)
    plt.show()
    print(round(Psys), "/", round(Pdia))


if __name__ == '__main__':
    main()
