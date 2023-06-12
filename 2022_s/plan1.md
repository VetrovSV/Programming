```python
# класс — структурированный тип данных, определяемый программистом
class Student:
    # поля класс
    name: str = ""
    fname: str= ""
    group: str = ""
    grade: int = 0


# создание переменной - объекта (экземпляр класса)
s1 = Student()
# задание значений полям объекта (не класса!)
s1.name = "Антон"
s1.fname = "Мурзин"
s1.group = "СиСАК-22-2"
s1.grade = 4

s2 = Student()
s2.name = "Иван"
s2.fname = "Иванов"
s2.group = "СиСАК-22-2"
s2.grade = 5


s3 = Student()
s3.name = "Пётр"
s3.fname = "Петров"
s3.group = "СиСАК-22-2"
s3.grade = 2


s4 = Student()
s4.name = "Константин"
s4.fname = "Константинов"
s4.group = "СиСАК-22-2"
s4.grade = 3

# открытие файла для записи (w), текст будет сохранятся в универсальной кодировке (UTF8)
f = open('students.txt', 'w', encoding='utf-8')

# запись объектов в файл. одна строка - один объект
f.write( s1.name + " " + s1.fname + " " + s1.group + " " + str(s1.grade) + '\n')		# \n — сомвол перехода на новую строку
f.write( s2.name + " " + s2.fname + " " + s2.group + " " + str(s2.grade) + '\n')
f.write( s3.name + " " + s3.fname + " " + s3.group + " " + str(s3.grade) + '\n')
f.write( s4.name + " " + s4.fname + " " + s4.group + " " + str(s4.grade) + '\n')
# закрытие файла, запись всех данных их файлового буффера
f.close()

# список, куда будут помещены объекты, прочитанные из файла
students = []

# открытие файла для чтения
f2 = open('students.txt', encoding='utf-8')


for line in f2:					# построчное чтение файла, строки файла записываются в переменную цикла line
    words = line.split()		# разделение строки (разделить - пробел) на список подстрок,
    # создание объекта, заполнение полей из списка
    s = Student()
    s.name = words[0]
    s.fname = words[1]
    s.group = words[2]
    s.grade = int(words[3])

    # добавление объекта в список
    students.append( s )

    # вывод строки файла на экран (для наглядности)
    print(line, end="")

f2.close()

# вывод студентов, у кого оценка > 2
print()
for i in range(0, len(students)):				# перебор чисел от 0 до длины списка - 1
    s = students[i]     # s - Student
    if s.grade > 2:
        print( s.fname + " " + str(s.grade) )
```
