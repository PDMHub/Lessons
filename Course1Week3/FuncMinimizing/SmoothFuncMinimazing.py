from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
import sys, os


# Функция отрисовки результатов оптимизации
def draw_optimization_result(x0, x, y, title, result):
    plt.title(title)
    plt.plot(x, y)
    plt.plot(
        result['x'],
        result['fun'],
        'o',
        label='Initial guess = {0}'.format(x0))
    plt.legend()
    plt.show()


# Целевая функция на промежутке [1, 30]
x = np.linspace(1, 30, 30)
def f(x):
    return np.sin(x / 5.0) * np.exp(x / 10.0) + 5.0 * np.exp(-x / 2.0)

x_0 = 4.0
optimize_result = optimize.minimize(f, x0 = x_0, method = 'Nelder-Mead')
if optimize_result['success']:
    draw_optimization_result(x_0, x, f(x), "Nelder-Mead optimization method",
                             optimize_result)
    print("optimize_result = {0}".format(optimize_result))

x_0 = 4.0
optimize_result = optimize.minimize(f, x0 = x_0, method = 'BFGS')
if optimize_result['success']:
    draw_optimization_result(x_0, x, f(x), "BFGS optimization method",
                             optimize_result)
    print("optimize_result = {0}".format(optimize_result))

x_0 = 2.0
optimize_result = optimize.minimize(f, x0 = x_0, method = 'Nelder-Mead')
if optimize_result['success']:
    draw_optimization_result(x_0, x, f(x), "Nelder-Mead optimization method",
                             optimize_result)
    print("optimize_result = {0}".format(optimize_result))

# записываем в файл значение функции для первого приближения
with open('C:\\Lessons\\Course1Week3\\FuncMinimizing\\Optimization_Results.txt', 'w') as file_obj:
    file_obj.writelines(str(np.round(optimize_result['fun'], 2)) + ' ')

x_0 = 30.0
optimize_result = optimize.minimize(f, x0 = x_0, method = 'Nelder-Mead')
if optimize_result['success']:
    draw_optimization_result(x_0, x, f(x), "Nelder-Mead optimization method",
                             optimize_result)
    print("optimize_result = {0}".format(optimize_result))

# записываем в файл значение функции для второго приближения
with open('C:\\Lessons\\Course1Week3\\FuncMinimizing\\Optimization_Results.txt', 'a') as file_obj:
    file_obj.writelines(str(np.round(optimize_result['fun'], 2)) + ' ')
