import numpy as np
import scipy.linalg as sl


def LA(xk):
    return (10 / 3) * (1 - (1 / 40) * pow(xk + 1, -1))


def LD(xk):
    return (10 / 3) * (1 + (1 / 40) * pow(xk + 1, -1))


def LC(xk):
    return -(20 / 3)


def Fk(xk):
    return 1 / (30 * np.sqrt(xk + 1))


def f(xk):
    return (2 / 3) * pow(xk + 1, 3 / 2) + (1 / 3)


def TDMA_solve(a, b):
    u = 1
    l = 1
    n = 11
    m = 11
    ab = np.zeros((u + l + 1, m))
    for j in range(m):
        for i in range(n):
            index = u + i - j
            if 0 <= index < u + l + 1:
                ab[index][j] = a[i][j]
    ans = sl.solve_banded((l, u), ab, b)
    return ans


if __name__ == '__main__':
    a = 0
    b = 1
    h = 0.1
    n = int((b - a) / h)

    conditions = {
        'A': (6.3, -3),
        'C': (1.2, 0),
        'D': (-5.7, 3),
        'F': (0.6, 0.6 * np.sqrt(2))
    }

    x = [a + i * h for i in range(n + 1)]
    la = [LA(xk) for xk in x]
    lc = [LC(xk) for xk in x]
    ld = [LD(xk) for xk in x]

    fk = [Fk(xk) for xk in x]

    div_a = la[0] / conditions['A'][0]
    div_d = ld[10] / conditions['D'][1]

    c0 = lc[0] - conditions['C'][0] * div_a
    d0 = ld[0] - conditions['D'][0] * div_a
    f0 = fk[0] - conditions['F'][0] * div_a

    a10 = la[-1] - conditions['A'][1] * div_d
    c10 = lc[-1] - conditions['C'][1] * div_d
    f10 = fk[-1] - conditions['F'][1] * div_d

    solve = np.array([
        [c0, d0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [la[1], lc[1], ld[1], 0, 0, 0, 0, 0, 0, 0, 0],
        [0, la[2], lc[2], ld[2], 0, 0, 0, 0, 0, 0, 0],
        [0, 0, la[3], lc[3], ld[3], 0, 0, 0, 0, 0, 0],
        [0, 0, 0, la[4], lc[4], ld[4], 0, 0, 0, 0, 0],
        [0, 0, 0, 0, la[5], lc[5], ld[5], 0, 0, 0, 0],
        [0, 0, 0, 0, 0, la[6], lc[6], ld[6], 0, 0, 0],
        [0, 0, 0, 0, 0, 0, la[7], lc[7], ld[7], 0, 0],
        [0, 0, 0, 0, 0, 0, 0, la[8], lc[8], ld[8], 0],
        [0, 0, 0, 0, 0, 0, 0, 0, la[9], lc[9], ld[9]],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, a10, c10],
    ])

    _y = [f0, *fk[1:-1], f10]
    res = TDMA_solve(solve, _y)
    y = [f(xk) for xk in x]

    rn = [abs(p1 - p2) for p1, p2 in zip(res, y)]

    print(f'Точное решение:\n{y}')
    print(f'Приближенное решение:\n{res}')
    print(f'Разница:\n{rn}')