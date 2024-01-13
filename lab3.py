import numpy as np
import matplotlib.pyplot as plt


def w(x_arg, y_arg):
    return x_arg**3 + 2*x_arg**2


def v(x_arg, y_arg):
    return v_het(x_arg, y_arg) + h(x_arg, y_arg)


def v_het(x_arg, y_arg):
    return 3*b*y_arg - a * x_arg


def h(x_arg, y_arg):
    return h1(x_arg, y_arg) + h2(x_arg, y_arg)


def h1(x_arg, y_arg):
    sum = 0
    for i in range(1, n+1):
        sum += (a1(i) * np.e**(-np.pi * i * x_arg / b) + b1(i) * np.e**(np.pi * i * x_arg / b)) * np.sin(np.pi * i * y_arg / b)
    return sum

def a1(n_arg):
    #return 12 * b**2 * ((-1)**n_arg - 1)/(np.pi**3 * n_arg**3) - b1(n_arg)
    return 6 * (b ** 2) * (((-1) ** n_arg) - 1) * (np.e ** (np.pi * n_arg * a / b) - 1) / (np.pi ** 3 * n_arg ** 3 * np.sinh(
        np.pi * n_arg * a / b))


def b1(n_arg):
    #return 12 * b**2 * ((-1)**n_arg - 1) / (np.pi**3 * n_arg**3) * (1 - np.e**(-np.pi*n_arg*a/b)) / (np.e**(np.pi*n_arg*a/b) - np.e**(-np.pi*n_arg*a/b))
    return 6 * b ** 2 * (((-1) ** n_arg) - 1) * (1-np.e ** (-np.pi * n_arg * a / b)) / (np.pi ** 3 * n_arg ** 3 * np.sinh(
        np.pi * n_arg * a / b))

def h2(x_arg, y_arg):

    sum = 0
    for i in range(1, n+1):
        sum += (a2(i) * np.e**(-np.pi * i * y_arg / a) + b2(i) * np.e**(np.pi * i * y_arg / a)) * np.sin(np.pi * i * x_arg / a)
    return sum


def a2(n_arg):
    #return 4 * a ** 2 * ((-1) ** n_arg - 1) / (np.pi ** 3 * n_arg ** 3) - b2(n_arg)
    return -2 * a**2 * ((-1)**n_arg - 1) * (np.e**(np.pi*b/a)-1) / (np.pi**3 * n_arg**3 * np.sinh(np.pi*n_arg*b/a))


def b2(n_arg):
    # return 4 * a ** 2 * ((-1) ** n_arg - 1) / (np.pi ** 3 * n_arg ** 3) * (1 - np.e ** (-np.pi * n_arg * b / a)) / (
    #             np.e ** (np.pi * n_arg * b / a) - np.e ** (-np.pi * n_arg * b / a))
    return -2 * a**2 * ((-1)**n_arg - 1) * (1-np.e**(-np.pi*b/a)) / (np.pi**3 * n_arg**3 * np.sinh(np.pi*n_arg*b/a))


def u(x_arg, y_arg):
    return v(x_arg, y_arg)+w(x_arg, y_arg)


a = 1
b = 1
n = 100

x = np.linspace(0, 1, n)
y = np.linspace(0, 1, n)
X, Y = np.meshgrid(x, y)
Z = u(X, Y)
# values = []
# for x_vector, y_vector in zip(X, Y):
#      values.append([])
#      for x_i, y_i in zip(x_vector, y_vector):
#          print(x_i, y_i, u(x_i, y_i))
#          values[len(values)-1].append(u(x_i, y_i))
#
# values = np.array(values)

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, np.array(Z))
ax.set_xlabel(r'x')
ax.set_ylabel(r'y')
plt.show()

# x = np.linspace(0, 1, 10)
# y = 0
# y1 = 0.5
# y2 = 1
#
# z = u(x, y)
# z1 = u(x, y1)
# z2 = u(x, y2)
# plt.plot(x, z, label='y=0')
# plt.plot(x, z1, label='y=0.5')
# plt.plot(x, z2, label='y=1')
# plt.legend()
# plt.show()