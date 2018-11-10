#%%
from sympy import *
# import matplotlib.pyplot as plt
# import matplotlib as mpl
x, y, z = symbols('x y z ')
init_printing(use_latex = True)
#init_session(quiet=True, use_latex=True)
expr = exp(x)*(4*y-x*y-y**2)
deriv_x = diff(expr, x)
deriv_y = diff(expr, y)
deriv_x, deriv_y

# from sympy import *
# x,y,z = symbols('x y z ')
# init_printing(pretty_print = True)
# Integral(sqrt(1/x), x)
