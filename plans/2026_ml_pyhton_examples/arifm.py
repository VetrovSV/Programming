# вычислить значение функции Гаусса в точке x

# import math
from math import pi,\
                 sqrt,\
                 exp
# from math import *
import math as M

x:float = 0.0
y:float = 0.0

print("x = ", end="")
x = float( input() )

y = 1.0 / M.sqrt(2 * M.pi ) * M.exp( -x**2 / 2.0 )

print( f"y = {y:.4f}" )
