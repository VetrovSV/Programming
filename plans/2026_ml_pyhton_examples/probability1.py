"""
Модуль по теории вероятностей
"""

from math import *


def std_norm_density(x: float) -> float:
    """Вычисляет и возвращает значение функции плотности стандартного нормального распределения в точке x

    :param x: точка, в которой нужно вычислить значение функции
    :returns: значение функции нормального распределения
    """
    y = 1.0 / sqrt(2 * pi ) * exp( -x**2 / 2.0 )
    return y


assert round(std_norm_density(0.0),8)  == 0.39894228
# assert round(std_norm_density(0.0),8)  == 0.39894228
# assert round(std_norm_density(0.0),8)  == 0.39894228
