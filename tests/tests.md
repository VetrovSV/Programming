## Пример. Простые операторы assert

```python
import math

def calc_hypotenuse(a: float = 3, b: float = 4) -> float:
    """
    Возвращает гипотенузу треугольника, a, b — катеты
    :param a: катет 1, a>0
    :param b: катет 2, b>0
    :return: гипотенуза

    :raise ValueError: Бросает исключение, если a <= 0 или b <= 0
    """
    if a > 0 and b > 0:
        return (a*a + b*b)**0.5
    else:
        raise ValueError("Один или несколько катетов меньше или равны нулю")


def test_calc_hypotenuse():
    """Простые тесты через оператор assert для функции calc_hypotenuse"""
    assert calc_hypotenuse(3.0, 4.0) == 5.0             # треугольник с углами 30, 60 и 90
    # проверки с точностью 0.000_000_001
    assert abs( calc_hypotenuse(1.0, 1.0) - 1.414213562 ) < 0.00_000_000_1     # треугольник с углами 45, 45 и 90
    assert abs( calc_hypotenuse(1.0, 2.0) - 2.236067977 ) < 0.00_000_000_1    # произвольный прямоугольный треугольник

    # сделать проверку с точностью можно также с помощью функции math.isclose
    assert math.isclose(calc_hypotenuse(1.0, 1.0), 1.414213562, rel_tol=1e-9)       # rel_tol=1e-9 - точность
    # isclose вернёт True если первый и второй аргумент отличаются меньше чем на rel_tol

    # проверка брошенного исключения
    try:
        calc_hypotenuse(0, 1)
    except ValueError:      # в норме, если функция работает корректно, она должна бросить исключение для ошибочных параметров
        pass
    else:
        # этот блок выполнится, если не сработал блок except
        assert False, "Ожидался ValueError при a=0"
        
    print("[PASS] test_calc_hypotenuse")


test_calc_hypotenuse()
```


Функцию тестирования `test_calc_hypotenuse` стоит вызывать в модуле, чтобы при подключении сразу тестировать его функции. Стоит использовать тесты для этапа разработки. Потом отключить assert для режима релиза через ключ -O: `python3 -O main.py`. Ключ `-O` включает оптимизацию, выключает отладочные возможности, в том числе проверку assert. Отдельного ключа для выключения assert в Питоне нет.

`assert` также полезно использовать в коде, чтобы контролировать важные инварианты во время решения задачи МО. Например, проверять все ли данные загрузились из файла; не пропали ли признаки или объекты при обработке этих данных; имеет ли модель удовлетворительную точность.

### Интеграция тестов в PyCharm
Если в PyCharm установлен пакет pytest, то можно запускать тесты в файле из IDE. Например:
контекстное меню файла (например test.py) > run pytest in test.py.
Отдельные вызовы assert не распознаются, но все функции содержащие assert могут быть распознаны как тестовые.



## Пример: pytest
```python

# test_geometry.py - отдельный файл с тестами. 
# Согласно правилам pytest этот файл должен начинается на test_
# рекомендуется поместить тесты в отдельную папку test
from math import sqrt

import pytest       # пакет для модульного тестирования (pip install pytest==8.4.2)
from geometry import calc_hypotenuse


# пример примитивной проверки. pytest обнаружит здесь вызов assert и обработает его
# имя тестовой функции должно начинаися на test_
def test_calc_hypotenuse_simple():
    # простая точная проверка
    assert calc_hypotenuse(3.0, 4.0) == 5.0


# пример однотипной проверки но для различных данных
# @pytest.mark.parametrize описывает набор тестовых данных
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1.0, 1.0, 1.414213562),
        (1.0, 2.0, 2.236067977),
        (5.0, 12.0, 13.0),
    ],
)
def test_calc_hypotenuse_parametrized(a, b, expected):
    # для сравнения чисел с плавающей точкой удобнее pytest.approx
    assert calc_hypotenuse(a, b) == pytest.approx(expected, rel=1e-9)
    # функция test_calc_hypotenuse_parametrized будет запущена для каждого варинта тестовых данных, т.е. 3 раза



# проверяем, что функция бросает ожидаемое исключение
def test_calc_hypotenuse_invalid():
    with pytest.raises(ValueError):
        calc_hypotenuse(0, 1)
    with pytest.raises(ValueError):
        calc_hypotenuse(-1, 2)

```


## См. также
- Документацию и примеры из пакета pytest
- настройку проекта для автоматизации запуска тестов
- интеграцию запуска тестов в IDE