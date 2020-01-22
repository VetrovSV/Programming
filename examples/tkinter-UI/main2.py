"""
Вариант программы с текстовым интерфейсом.
Вариант с графическим интерфейсом см. в main.py
"""

from database import *


FILENAME = "mydatabase.csv"  # ...

Data = []   # ...


def print_data(data: list):
    """
    Показывает данные
    :param data:
    :return:
    """
    for record in data:
        print(record.name, record.violation, record.date, record.sum)



def add_record(data: list):
    """
    Запрашивает данные у пользователя и добавляет в БД
    :param data:
    :return:
    """
    record = Violation()
    print("Введите данные о нарушении")
    print("Нарушитель: ", end="")
    record.name = input()
    # ...
    print("Сумма штрафа: ", end="")
    record.sum = float ( input() )
    data.append( record )


def del_record(data: list):
    """
    ...
    :param data:
    :return:
    """
    pass


def edit_record(data: list):
    """
    ...
    :param data:
    :return:
    """
    pass


def exit_progr(data: list):
    #  ....
    save_databese(data, FILENAME)
    # ....




def asq_action(data: list):
    """
    Запрашивает действие у пользователя и выполняет его
    :param data:
    :return:
    """
    while True:
        print("Выберете действие")
        print("1 - показать таблицу")
        print("2 - добавить запись")
        print("3 - удалить запись")
        print("4 - редактировать запись в таблице")
        print("0 - выход (данные сохранятся автоматически)")
        action = input("> ")

        if action == "1":
            print_data(data)
        elif action == "2":
            add_record(data)
        elif action == "3":
            del_record(data)
        elif action == "4":
            edit_record(data)
            # ....
        elif action == "0":
            exit_progr(data)
            break




Data = load_database(FILENAME)
asq_action(Data)


