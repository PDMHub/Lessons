import sympy as sp

from sympy.plotting import plot, plot_parametric 
#%matplotlib inline
init_printing()
x, f1, f2, f3 = symbols('x, f1, f2, f3')

# Функция, ограниченная при всех
# x, принадлежащих R
f = sp.sin(x)

# Функция, ограниченная сверху, при всех
# x (-00; 0]
f1 = 1/x

# Функция, ограниченная снизу при всех
# x, принадлежащих R
f2 = sp.Abs(x)

p1 = plot(f1)
p2 = plot(f2)
p3 = plot(f3)




