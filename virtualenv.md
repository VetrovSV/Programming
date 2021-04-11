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

Создаем новое окружение\
`virtualenv <my_env_name>` 	

Будет создана папка `my_env_name` с нужными питону файлами

Активировать можно так: `my_env_name/Scripts/activate.bat`\
Далее можно устанавливать пакеты пользуясь pip из этой же папки


# Ссылки
https://pypi.org/project/virtualenv/

https://habr.com/ru/post/491916/ -- Создание виртуальных окружений и установка библиотек для Python 3 в IDE PyCharm
