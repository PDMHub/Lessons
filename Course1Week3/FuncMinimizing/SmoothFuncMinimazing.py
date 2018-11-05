from scipy import optimize
<<<<<<< HEAD
import matplotlib.pyplot as plt
=======
import matplotlib.pyplot as plt 
>>>>>>> 02dbceae7bf47eb22e31c27102c2f743c6625798
import numpy as np
import math

# Целевая функция
def f(x):
    return math.sin(x / 5.0) * math.exp(x / 10.0) + 5.0 * math.exp(-x / 2.0)

y=[]
for x in range(0, 30, 2):
    y.append(f1(x))

y = []
for x in range(1, 30, 2):
    y.append(f(x))
print(y)

optimize_result = optimize.minimize(f, x0=np.array([3.0]))
if optimize_result['success']:
    x_min = optimize_result['x']
    print(x_min)

<<<<<<< HEAD
plt.plot(range(0, 30, 2), y)
plt.show()
=======
plt.plot(range(1, 30, 2), y)
plt.show()
>>>>>>> 02dbceae7bf47eb22e31c27102c2f743c6625798
