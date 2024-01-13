import numpy as np


def solve_linear(x):
    return (x / 2) + (1 / 2) * np.sin(x) + 0.10923879 * x - 1.37634757 * np.power(x, 2) - 0.06443955 * np.power(x, 3)


if __name__ == '__main__':
    for x in np.arange(0, 1.1, 0.1):
        if x == 0.30000000000000004:
            x = 0.3
        elif x == 0.6000000000000001:
            x = 0.6
        elif x == 0.7000000000000001:
            x = 0.7
        solve_linear(x)
        print(f'For x = {x} \t u(x) = {solve_linear(x)}')
