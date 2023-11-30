from typing import Callable


def collocation_method(exact_solution: Callable, numerical_solution: Callable, a: float, b: float):
    tabulate_array = [
        '\\hline'
    ]
    error_value = []

    while a <= b:
        tabulate_array.append(a)
        tabulate_array.append('&')
        tabulate_array.append(exact_solution(a))
        tabulate_array.append('&')
        tabulate_array.append(numerical_solution(a))
        tabulate_array.append('&')
        tabulate_array.append(abs(exact_solution(a) - numerical_solution(a)))
        error_value.append(abs(exact_solution(a) - numerical_solution(a)))
        tabulate_array.append('\\\\ \n \\hline')
        a += 0.1
    print(*tabulate_array)
    print('Ошибка:', *error_value)


def exact_sol(x):
    return 2/3 * (x+1)**(3/2) + 1/3


def numerical_sol(x):
    return -0.026412 * x**3 + 0.24271143 * x**2 + 1.00802670 * x + 1.00535113


if __name__ == '__main__':
    collocation_method(exact_sol, numerical_sol, 0, 1)
