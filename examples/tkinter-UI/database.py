# модуль с описанием бизнес-логики, типов данных, функций для работы с ними

# нарушение
class Violation:
    name = ""           # ...
    violation = ""
    date = ""

    sum = 0.0


# Формат файла:
# ФИО нарушителя| описание нарушения| дата нарушения| сумма штрафа
# Иванов А. Б| сбил пешехода| 22.01.2020| 10000000
# Иванов И. Б| сбил пешехода| 20.01.2020| 100



def load_database(filename: str):
    """
    Возвращает список из записей базы данных
    :param filename: имя файла с данными
    """
    data = []

    f = open(filename,'r')

    for line in f:
        record0 = line.split('|')
        record = Violation()

        record.name = record0[0]
        record.violation = record0[1]
        record.date = record0[2]
        record.sum = float(record0[3])

        data.append( record )

    f.close()

    return data


def save_databese(data:list, filename:str):
    """
    :param data: ...
    :param filename:  ..
    :return:
    """
    f = open(filename,'w')
    for record in data:
        f.write( record.name )
        f.write("|")
        f.write(record.violation )
        f.write("|")
        f.write(record.date)
        f.write("|")
        f.write(str(record.sum))
        f.write('\n')
    f.close()


