"""
Модуль с простыми тестами

Запуск тестов: pytest
Запуск тестов с выводом всех тестовых функций : pytest

Pytest сам обнаружит файлы с тестами (test_*.py) и запустит там все функции

Подробности:
https://docs.pytest.org/en/stable/getting-started.html
"""

import pytest
import my_statistics

def test_mean():
    assert my_statistics.mean([]) is None
    assert my_statistics.mean([1.2]) == 1.2
    assert my_statistics.mean([1, 2, 3]) == 2.0
    assert my_statistics.mean([-1, -2, -3]) == -2.0


def test_std():
    assert my_statistics.std([]) == 0.0
    assert my_statistics.std([1.2]) == 0.0
    assert my_statistics.std([1, 2, 3]) == pytest.approx( 0.816496580927726 )
    assert my_statistics.std([-1, -2, -3]) == pytest.approx( 0.816496580927726 )
    # пример сломанного теста
    # assert my_statistics.std([-1, -2, -3]) == 0

# pytest.approx — это объект со специальным сравнением, который переопределяет операцию ==, чтобы с допуском (погрешностью) сравнивать числа
