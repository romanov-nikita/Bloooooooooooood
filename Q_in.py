from math import sin, cos, gamma, pi, sqrt
from scipy.misc import derivative

# class for pulsative cardiac output simulation
class Q_in():

    def __init__(self, HR, SV, n=13, phi=pi / 10):
        """Constructor
            HR: heart rate
            SV: stroke volume
            n: degree of sin in Q_in (default is 13 == systole is 1/3 of cardiac cycle)
            phi: phase angle (default is pi/10)"""
        self.HR = HR
        self.SV = SV
        self.n = n
        self.phi = phi

    def T(self):
        """Period"""
        return 60 / self.HR

    def w(self):
        """Frequency"""
        return pi / self.T()

    def A(self):
        """Normalizing coefficient"""
        return ((sqrt(pi) * gamma(1 + self.n / 2) * sin(self.phi)) / gamma(
            (3 + self.n) / 2)) / self.w()

    def Q(self, t):
        """Function of pulsative cardiac output"""
        # offset to the beginning of diastole
        t += 0.2
        return self.SV / self.A() * (sin(self.w() * t) ** self.n) * cos(self.w() * t - self.phi)

    def Q_der1(self, t):
        """First derivative of pulsative cardiac output"""
        return derivative(self.Q, t, dx=1e-6)

    def Q_der2(self, t):
        """Second derivative of pulsative cardiac output"""
        return derivative(self.Q_der1, t, dx=1e-6)
