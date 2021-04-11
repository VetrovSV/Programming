# PyInstaller

`pip install pyinstaller`


# Создание исполняемого файла для программы с GUI

`pyinstaller --onefile --windowed myscript.py`

`--windowed` -- не показывать консольное окно

pyinstaller рекурсивно обработает все подключения библиотек.

После сборки исполняемый файл появится в папке dist. Используемые программой файлы (не библиотеки) придётся скопировать в папку с программой вручную. 


# Ссылки
https://www.pyinstaller.org/
