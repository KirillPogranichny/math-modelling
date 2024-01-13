import numpy as np
from matplotlib import pyplot as plt


def Xn(x, n):
    return np.sin(np.pi * n * x)


def lamda_n(n):
    return pow(np.pi, 2) * pow(n, 2)


def Tn(t, n, k):
    return ((k + (6*np.pi*n - 6*np.pi*n*np.cos(np.pi*n)) / pow(lamda_n(n)*np.pi*n, 2) -
            (2*np.pi*n*np.cos(np.pi*n)-2*np.sin(np.pi*n)) / (lamda_n(n)*pow(np.pi*n, 2))) * pow(np.e, -lamda_n(n)*t) +
            (6*np.pi*n - 6*np.pi*n*np.cos(np.pi*n))*t / (lamda_n(n)*pow(np.pi*n, 2)) +
            (2*np.pi*n*np.cos(np.pi*n)-2*np.sin(np.pi*n)) / (lamda_n(n)*pow(np.pi*n, 2)) -
            (6*np.pi*n - 6*np.pi*n*np.cos(np.pi*n)) / pow(lamda_n(n)*np.pi*n, 2))


def un(x, t, n):
    summary = 0
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

# (0, y) = 1
# (1, y) = y
