from math import sin, cos, gamma, pi, sqrt
from scipy.misc import derivative

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
        return derivative(self.Q, t, dx=1e-6)

    def Q_der2(self, t):
        return derivative(self.Q_der1, t, dx=1e-6)
