"""
Задание:
приблизить функцию f(x) = sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)
с помощью многолченов
"""

import numpy as np
from scipy import linalg
import math
import re


def make_b_vector(x_values):
    """
    Функция, принимающая введенные пользователем в консоли данные и превращающая их
    в в вектор b из уравнения Ax = b
    :param x_values: введенные пользователем в консоли данные
    :return: вектор b из уравнения Ax = b
    """
    y_values = []
    for xValue in x_values:
        y = math.sin(xValue / 5) * math.exp(xValue / 10) + 5 * math.exp(-xValue / 2)
        y_values.append(y)
    return y_values


def raise_items_to_power(lst: list):
    """
    Функция, возводящая в соотвествующую степень известные знаения иксов для какого-то n-ного уравнения из системы
    :param lst: вектор иксов, которые нужно возвести в соответствующие степени
    :return: этот же вектор иксов, но уже с возведенными в соотвествующую степень иксами
    """
    # начиная со 3-го члена в уравнении w0 + w1x + w2x^2 + w3x^3 + ... = f(x) иксы возводятся в степень
    # power, которая по сути равна индексу элемента в списке (начиная со 2-го элемента, с учетом нумерации с нуля)
    power = 2
    if len(lst) < 3:
        return lst
    else:
        for i in range(2, len(lst)):
            lst[i] = lst[i] ** power
            power += 1
        return lst


def make_a_matrix(lst: list):
    """
    Функция, создающая матрицу А из уравнения Ax = b
    в том виде, в котором ее ожидает функция scipy.linalg.solve(A,b)
    :param lst: список известных значений икс, которые пользователь ввел в консоли
    :return: матрица А из уравнения Ax = b
    """
    matrix = []
    for item in lst:
        # [item]*(len(lst)-1) - множим одинаковые значения в списке
        vector = [1] + [item]*(len(lst)-1)
        matrix.append(raise_items_to_power(vector))
    return matrix


x_values_input = input("Input 2, 3 or 4 x values divided by space: ")
x_values_list = [int(x_i) for x_i in re.split('[\s+]', x_values_input.lower()) if x_i]
a_matrix = make_a_matrix(x_values_list)
bVector = np.array(make_b_vector(x_values_list))

print('A matrix = ' + str(a_matrix))
print('b vector = ' + str(bVector))

answer1 = linalg.solve(a_matrix, bVector)
print(answer1)
