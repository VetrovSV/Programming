"""
Пример модуля, который нужно протестировать
"""

from math import sqrt


def mean( arr: list[float] ) -> float | None:
    """Вычисляет средне значение в массиве"""
    if len(arr) != 0:
        return sum(arr) / len(arr)
    else:
        return None


def std( arr: list[float] ) -> float:
    """Вычисляет стандартное отклонение в массиве"""
    if len(arr) >= 2:
        m = mean(arr)
        return sqrt(sum((x - m) ** 2 for x in arr) / len(arr))
    else:
        return 0.0
