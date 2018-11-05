from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np
import math


def f1(x):
    return math.sin(x / 5.0) * math.exp(x / 10.0) + 5.0 * math.exp(-x / 2.0)

y=[]
for x in range(0, 30, 2):
    y.append(f1(x))

optimize_result = optimize.minimize(f1, x0=np.array([30.0]))
if optimize_result['success']:
    x_min = optimize_result['x']
    print(x_min)

plt.plot(range(0, 30, 2), y)
plt.show()