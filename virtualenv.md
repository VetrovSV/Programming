# VirtualEnv

VirtualEnv используется для создания виртуальных окружений для Python программ. Это необходимо для избежания конфликтов, позволяя установить одну версию библиотеки для одной программы, и другу для второй.

### Установка

**Windows**
```bash
pip install virtualenv
pip install virtualenvwrapper-win
```


**Ubuntu**
```bash
pip3 install --user virtualenv virtualenvwrapper
```

### Работа с окружениями

`mkvirtualenv env-name` 	Создаем новое окружение
`workon` 	Смотрим список окружений
`workon env-name` 	Меняем окружение
`deactivate` 	Выходим из окружения
`rmvirtualenv env-name` 	Удаляем окружение



# Ссылки
https://pypi.org/project/virtualenv/

https://habr.com/ru/post/491916/ -- Создание виртуальных окружений и установка библиотек для Python 3 в IDE PyCharm
