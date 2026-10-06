import sys
from random import randint

HELP = """args_example.py [-h | --help] <n>
Программа генерирует случайные числа

n               -  количество случайных чисел в интервале от 0 до 100, которое будет сгенерировано программой
-h | --help     - вывод этой справки
"""

if len(sys.argv) < 2:
    print(HELP)
    exit(1)

if  sys.argv[1] == '-h' or \
    sys.argv[1] == '--help':
    print(HELP)
    exit(0)

n = int(sys.argv[1])

for i in range(n):
    print( randint(0,100), end = " " )

print()
