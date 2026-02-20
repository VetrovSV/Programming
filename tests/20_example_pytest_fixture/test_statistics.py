"""
Модуль с простыми тестами и фикстурой. Сравните этот файл с предыдущим примером.

Запуск тестов: pytest
Запуск тестов с выводом всех тестовых функций : pytest

Pytest сам обнаружит файлы с тестами (test_*.py) и запустит там все функции

Подробности:
https://docs.pytest.org/en/stable/getting-started.html
"""

import pytest
import my_statistics


# фикстура (fixture - приспособление) -- специальный код, который вызывается перед каждой тестовой функцией и в данном случае готовит для него тестовые данные.
# Таким образом если в тестовых функциях часто используются одни и те же данные, то их не придётся в каждой тестовой функции описывать
@pytest.fixture
def datasets():
    return {
        "empty" : [],
        "one_el" : [1.2],
        "3_el" : [1, 2, 3],
        "3_el_neg" : [-1, -2, -3],
    }
    # этот словарь хранит тестовые данные

# фикстуру нужно передавать в каждую тестовую функцию
def test_mean(datasets):
    assert my_statistics.mean( datasets["empty"] )  is  None
    assert my_statistics.mean( datasets["one_el"] )  ==  1.2
    assert my_statistics.mean( datasets["3_el"] )  ==  2.0
    assert my_statistics.mean( datasets["3_el_neg"] )  == -2.0


def test_std(datasets):
    assert my_statistics.std(datasets["empty"])     == 0.0
    assert my_statistics.std(datasets["one_el"])    == 0.0
    assert my_statistics.std(datasets["3_el"])      == pytest.approx( 0.816496580927726 )
    assert my_statistics.std(datasets["3_el_neg"])  == pytest.approx( 0.816496580927726 )
    # пример сломанного теста
    # assert my_statistics.std([-1, -2, -3]) == 0
