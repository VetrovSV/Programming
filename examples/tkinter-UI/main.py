#!/usr/bin/env python3

"""
основная программа
здесь приведены основные функции для работы с интерфейсом

Вариант с графическим интерфейсом
Вариант c текстовым интерфейсом. см. в main2.py
"""


from tkinter import *
from tkinter import filedialog
from tkinter import ttk  # для настройки стилей


from database import *

# для хранения БД
Data = []



def open_file(event):
    """ Показываает диалог для открытия файла, 
    Загружает данные из файла
    """
    global Tbale
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",
        filetypes = (("text files","*.csv"),("all files","*.*")))
    # open file, load data


def del_rec(event): 
    """ Обработчик события: нажатие кнопки 'удалить' в диалоговом окне из show_rec_del_window
    Удаляет данные из таблицы, обновляет главное окно
    """
    global spinbox_n, dialog_del
    n = spinbox_n.get()
    # удаление записи из табоицы
    # ...
    # обновление главного окна
    # ...
    dialog_del.destroy()


def show_rec_del_window(event):
    """ Показывает даилоговое окно для удаления записи таблицы
    """
    global dialog_del, spinbox_n
    dialog_del = Toplevel()
    label = Label(dialog_del, text="Номер записи")
    spinbox_n = Spinbox(dialog_del, from_=0, to=10)
    btn = Button(dialog_del, text="OK")
    label.pack()
    spinbox_n.pack()
    btn.pack()
    btn.bind('<Button-1>', del_rec)


def create_mainwindow():
    """ Создаёт главное окно
    """
    root = Tk()

    frame_buttons = Frame(root)
    btn_open = Button(frame_buttons, text = "open file")
    btn_save = Button(frame_buttons, text = "save file")
    btn_add = Button(frame_buttons,  text = "add")
    btn_del = Button(frame_buttons,  text = "del")

    btn_open.pack(side=LEFT, padx=PADX)
    btn_save.pack(side=LEFT, padx=PADX)
    btn_add.pack(side=LEFT, padx=PADX)
    btn_del.pack(side=LEFT, padx=PADX)

    btn_open.bind('<Button-1>', open_file)
    btn_del.bind('<Button-1>', show_rec_del_window)

    frame_buttons.pack()

    main_text = Text()  # текстовое поле (будет использовано для вывода данных)
    main_text.pack(fill=BOTH, expand=True)

    return root



# горизонтальное расстояние между кнопками
PADX = 6


# диалоговое окно удаления записи
dialog_del = None
# спинбокс для ввода номера записи
spinbox_n = None

root = create_mainwindow()
root.mainloop()