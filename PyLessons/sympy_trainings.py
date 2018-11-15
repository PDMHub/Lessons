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

#%%
from sympy import *
from sympy.physics.vector import ReferenceFrame, dot
# Система отсчета
N = ReferenceFrame('N')
from sympy import vector
x1, x2 , y1, y2, z1, z2 = symbols('x1 x2 y1 y2 z1 z2')
v1 = x1*N.x + y1*N.y + z1*N.z
v2 = x2*N.x + y2*N.y + z2*N.z
dot(v1, v2)


#%%
from sympy import MatMul, MatrixSymbol
A = MatrixSymbol('A', 3, 1)
B = MatrixSymbol('B', 1, 3)
MatMul(A, B)