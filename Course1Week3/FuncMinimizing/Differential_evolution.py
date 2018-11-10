#%%

from scipy.optimize import differential_evolution
import matplotlib.pyplot as plt
import numpy as np
import sys, os

#%matplotlib inline 
# Функция отрисовки результатов оптимизации
def draw_optimization_result(bounds, x, y, title, result):
    plt.title(title)
    plt.plot(x, y)
    plt.plot(
        result['x'], result['fun'], 'o', label='Bounds = {0}'.format(bounds))
    plt.legend()
    plt.show()


# Целевая функция на промежутке [1, 30]
x = np.linspace(1, 30, 30)


def f(x):
    return np.sin(x / 5.0) * np.exp(x / 10.0) + 5.0 * np.exp(-x / 2.0)


bounds = [(1, 30)]

optimize_result = differential_evolution(f, bounds)
if optimize_result['success']:
    draw_optimization_result(bounds, x, f(x), "Differential evolution",
                             optimize_result)
    print("optimize_result = {0}".format(optimize_result))

# записываем в файл значение функции для второго приближения
with open('C:\\Lessons\\Course1Week3\\FuncMinimizing\\Evolution_results.txt', 'w') as file_obj:
    file_obj.writelines(str(np.round(optimize_result['fun'][0], 2)) + ' ')

