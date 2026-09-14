# вывести значение функции плотности стандартного нормального распределения от x = 0, до тех пор пока функция не станет < 0.001

from math import *

MIN_Y = 0.001
x:float = 0.0
dx:float = 0.1
y:float = 0.0


y = 1.0 / sqrt(2 * pi ) * exp( -x**2 / 2.0 )

while y >= MIN_Y :
    print( f"x = {x:.4f}, y = {y:.4f}" )
    x += dx
    y = 1.0 / sqrt(2 * pi ) * exp( -x**2 / 2.0 )
