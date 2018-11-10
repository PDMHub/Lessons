#%%
#%matplotlib inline

from scipy.optimize import minimize
from scipy.optimize import differential_evolution
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
        label='Initial conditions = {0}'.format(x0))
    plt.legend()
    plt.show()


# Целевая функция на промежутке [1, 30]
x = np.linspace(1, 30, 30)
def f(x):
    res = np.sin(x / 5.0) * np.exp(x / 10.0) + 5.0 * np.exp(-x / 2.0)
    return np.round(res, decimals=0)
    #return np.array(x, dtype = 'int32')


# Поскольку градиента для негладкой функции не существует
# метод BFGS в данном случае непригоден для поиска экстремума
x_0 = 22.0
optimize_result = minimize(f, x0 = x_0, method = 'BFGS')
if optimize_result['success']:
    draw_optimization_result(x_0, x, f(x), "BFGS optimization method",
                             optimize_result)
    print("optimize_result = {0}".format(optimize_result))


# записываем в файл значение функции для первого приближения
with open('C:\\Lessons\\Course1Week3\\FuncMinimizing\\NonSmooth_Results.txt', 'w') as file_obj:
    file_obj.writelines(str(np.round(optimize_result['fun'][0], 2)) + ' ')

bounds = [(1, 30)]

optimize_result = differential_evolution(f, bounds)
if optimize_result['success']:
    draw_optimization_result(bounds, x, f(x), "Differential evolution",
                             optimize_result)
    print("optimize_result = {0}".format(optimize_result))

# записываем в файл значение функции для второго приближения
with open('C:\\Lessons\\Course1Week3\\FuncMinimizing\\NonSmooth_Results.txt',
          'a') as file_obj:
    file_obj.writelines(str(np.round(optimize_result['fun'], 2)) + ' ')
