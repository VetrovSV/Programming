# вывести значение функции плотности стандартного нормального распределения от x = -3, до +3, количество шагов - n

from math import *

X0 = -3.0
X1 = +3.0

x:float = X0
n:int = 5
dx:float = (X1 - X0) / (n-1)
y:float = 0.0



for i in range(n):
    y = 1.0 / sqrt(2 * pi ) * exp( -x**2 / 2.0 )
    print( f"x = {x:8.4f}, y = {y:8.4f}" )

    x += dx
