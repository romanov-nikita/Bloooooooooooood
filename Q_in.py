from math import sin, cos, gamma, pi, sqrt
from scipy.misc import derivative
import matplotlib.pyplot as plt


class Q_in():

    def __init__(self, HR, SV, n=13, phi=pi / 10):
        """Constructor"""
        self.HR = HR
        self.SV = SV
        self.n = n
        self.phi = phi

    def T(self):
        return 60 / self.HR

    def w(self):
        return pi / self.T()

    def A(self):
        return ((sqrt(pi) * gamma(1 + self.n / 2) * sin(self.phi)) / gamma(
            (3 + self.n) / 2)) / self.w()

    def Q(self, t):
        t += 0.2
        return self.SV / self.A() * (sin(self.w() * t) ** self.n) * cos(self.w() * t - self.phi)

    def Q_der1(self, t):
        t += 0.2
        return self.SV / self.A() * (self.n * self.w() * cos(self.w() * t) * sin(self.w() * t) ** (self.n - 1) * cos(
            self.w() * t - self.phi) - self.w() * sin(self.w() * t) ** self.n * sin(self.w() * t - self.phi))

    def Q_der2(self, t):
        t += 0.2
        return self.SV / self.A() * (-self.w() ** 2) * sin(self.w() * t) ** (self.n - 2) * (
                    (1 - self.n) * self.n * cos(self.w() * t - self.phi) + (self.n + 1) * sin(self.w() * t) ** 2 * cos(
                self.w() * t - self.phi) + 2 * self.n * sin(self.w() * t) * cos(self.w() * t) * sin(
                self.w() * t - self.phi))

    def getPlot(self):
        dt = 0.001
        nmax = int(self.T() // dt)
        t = [0] * (nmax + 1)
        t = [i * dt for i in range(0, nmax + 1)]
        Qin_der1 = [self.Q_der1(i * dt) for i in range(0, nmax + 1)]
        Qin_der1_my = [self.Q_der11(i * dt) for i in range(0, nmax + 1)]
        plt.plot(t, Qin_der1, "b")
        plt.plot(t, Qin_der1_my, "r")
        plt.show()