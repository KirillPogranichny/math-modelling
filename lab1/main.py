from pydantic import BaseModel
from typing import Callable
import numpy as np


def condition_function(x, y):
    return 2 * np.e ** x - y


def cauchy_problem_analytic_solution(x):
    return 1 / 2 * (np.e ** x + np.e ** (-x))


class NumericExperiments(BaseModel):
    f_x_y: Callable = condition_function
    cauchy_problem_analytic_solution: Callable = cauchy_problem_analytic_solution
    y_0: int = 1
    a: int = 0
    b: int = 1
    h: int = 0.1
    __euler_values = []
    __improved_euler_values = []
    __runge_kutta_values = []
    __exact_values = []

    def __tabulate_experiment(self, exact_array, num_array):
        tabulate_array = ['\\hline']
        x_i = self.a
        for exact_value, num_value in zip(exact_array, num_array):
            tabulate_array.append(x_i)
            tabulate_array.append('&')
            tabulate_array.append(exact_value)
            tabulate_array.append('&')
            tabulate_array.append(num_value)
            tabulate_array.append('&')
            tabulate_array.append(abs(exact_value - num_value))
            tabulate_array.append('\\\\ \n \\hline')
            x_i += 0.1

        return tabulate_array

    def __do_euler_method(self):
        x_i = self.a
        y_i = self.y_0
        calculated_values: [int] = [self.y_0]
        while x_i < self.b:
            y_i = y_i + self.h * self.f_x_y(x_i. y_i)
            calculated_values.append(y_i)
            x_i += self.h
        return calculated_values

    def __get_exact_values(self):
        x_i = self.a + self.h
        calculated_values: [int] = [self.y_0]
        while x_i <= self.b:
            calculated_values.append(cauchy_problem_analytic_solution(x_i))
            x_i += self.h
        return calculated_values

    def execute_lab(self):
        self.__euler_values = self.__do_euler_method()
        self.__exact_values = self.__get_exact_values()
        self.__improved_euler_values = self.__improved_euler_method()
        self.__runge_kutta_values = self.__runge_kutta_method()

        euler_improved = self.__tabulate_experiment(self.__exact_values, self.__runge_kutta_values)
        for value in euler_improved:
            print(value)

    def __improved_euler_method(self):
        x_i = self.a
        y_i = self.y_0
        calculated_values: [int] = [self.y_0]
        iterator = 0
        while x_i < self.b:
            y_i += self.h / 2 * (self.f_x_y(x_i, y_i) + self.f_x_y(x_i+self.h, self.__euler_values[iterator+1]))
            calculated_values.append(y_i)
            x_i += self.h
            iterator += 1
        return calculated_values

    def __runge_kutta(self):
        calculated_values: [int] = [self.y_0]
        x_i = self.a
        y_i = self.y_0
        while x_i < self.b:
            k_1 = self.f_x_y(x_i, y_i)
            k_2 = self.f_x_y(x_i+self.h/2, y_i+self.h*k_1/2)
            k_3 = self.f_x_y(x_i+self.h/2, y_i+self.h*k_2/2)
            k_4 = self.h * self.f_x_y(x_i+self.h, y_i+self.h*k_3)
            y_i += self.h/6 * (k_1 + 2 * k_2 + 2 * k_3 + k_4)
            calculated_values.append(y_i)
            x_i += self.h
        return calculated_values

    def __draw_plots(self):
        pass

    def __draw_table(self):
        pass


if __name__ == 'main':
    NumericExperiments()
