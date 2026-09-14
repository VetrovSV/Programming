"""
вывести  от x = -3, до +3, количество шагов - n
"""

__author__ = 'Sergey'



import probability1


# help(std_norm_density)

X0 = -3.0
X1 = +3.0

x:float = X0
n:int = 5
dx:float = (X1 - X0) / (n-1)
y:float = 0.0

for i in range(n):
    y = probability1.std_norm_density(x)
    print( f"x = {x:8.4f}, y = {y:8.4f}" )

    x += dx
