from random import randint

def random_ascending_numbers( n: int, b:int ) -> int:
    """Генератор целых возрастающих значений от 0 до +inf
    Возможно увеличение следующего числа на значение от 0 до b
    """
    prev = 0
    for i in range(n):
        tmp = prev + randint(0,b)
        yield tmp
        prev = tmp


for x in random_ascending_numbers(60, 10):
    print(x, end = " ")

print()
