import numpy as np
from matplotlib import pyplot as plt


def Xn(x, n):
    return np.sin(np.pi * n * x)


# def fn(t, n):
#     return 2 * ((np.sin(np.pi * n) - np.pi * n * np.cos(np.pi * n)) * np.sin(t) + 2 * np.sin(np.pi * n)
#                 - 3 * np.pi * n * np.cos(np.pi * n) + np.pi * n) / (pow(np.pi, 2) * pow(n, 2))


def lamda_n(n):
    return pow(np.pi, 2) * pow(n, 2)


def Tn(t, n, k):
    return ((k + (6*np.pi*n - 6*np.pi*n*np.cos(np.pi*n)) / pow(lamda_n(n)*np.pi*n, 2) -
            (2*np.pi*n*np.cos(np.pi*n)-2*np.sin(np.pi*n)) / (lamda_n(n)*pow(np.pi*n, 2))) * pow(np.e, -lamda_n(n)*t) +
            (6*np.pi*n - 6*np.pi*n*np.cos(np.pi*n))*t / (lamda_n(n)*pow(np.pi*n, 2)) +
            (2*np.pi*n*np.cos(np.pi*n)-2*np.sin(np.pi*n)) / (lamda_n(n)*pow(np.pi*n, 2)) -
            (6*np.pi*n - 6*np.pi*n*np.cos(np.pi*n)) / pow(lamda_n(n)*np.pi*n, 2))


def un(x, t, n):
    k = 0
    summary = 1 - x + x * t
    for i in range(1, n):
        if i == 4:
            summary += Xn(x, i) * Tn(t, i, 1)
        else:
            summary += Xn(x, i) * Tn(t, i, 0)
    return summary + x


a, b, N = 0, 1, 20
t = [0, .5, 1]
x = np.linspace(a, b, N)
for ti in t:
    u = un(x, ti, N)
    plt.plot(x, u)
    plt.show()
