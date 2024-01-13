import numpy as np
from matplotlib import pyplot as plt


def Xn(x, n):
    return np.sin(np.pi * n * x)


def fn(t, n):
    return 2 * ((np.sin(np.pi * n) - np.pi * n * np.cos(np.pi * n)) * np.sin(t) + 2 * np.sin(np.pi * n)
            - 3 * np.pi * n * np.cos(np.pi * n) + np.pi * n) / (pow(np.pi, 2) * pow(n, 2))


def lamda_n(n):
    return pow(np.pi, 2) * pow(n, 2)


def Tn(t, n):
    return ((((2 * pow(-1, n) - 2) / lamda_n(n)) - (fn(t, n) / (np.pi * n * lamda_n(n)))) * np.sin(np.pi * n * t)
            - np.cos(np.pi * n * t) * (fn(t, n) / lamda_n(n)) + (fn(t, n) / lamda_n(n)))


def un(x, t, n):
    summary = 0
    for i in range(1, n):
        summary += Xn(x, i) * Tn(t, i)
    return summary + x


a, b, N = 0, 1, 20
t = [0, .5, 1]
x = np.linspace(a, b, N)
for ti in t:
    u = un(x, ti, N)
    plt.plot(x, u)
    plt.show()
