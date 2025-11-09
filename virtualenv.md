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
`python3 -m venv my_env_name` 	

Будет создана папка `my_env_name` с нужными питону файлами.
Например:
```
├── myenv
│   ├── bin
│   │   ├── activate
│   │   ├── activate.csh
│   │   ├── activate.fish
│   │   ├── activate.ps1
│   │   ├── activate_this.py
│   │   ├── activate.xsh
│   │   ├── pip
│   │   ├── pip3
│   │   ├── pip-3.8
│   │   ├── pip3.8
│   │   ├── python -> /usr/bin/python3
│   │   ├── python3 -> python
│   │   ├── python3.8 -> python
│   │   ├── wheel
│   │   ├── wheel3
│   │   ├── wheel-3.8
│   │   └── wheel3.8
│   ├── lib
│   │   └── python3.8
│   └── pyvenv.cfg
```

Активировать можно так: `my_env_name/Scripts/activate.bat`\
Или так: `source my_env_name/bin/activate`\
Далее можно устанавливать пакеты пользуясь pip из этой же папки

При проблемах активации см: https://dev.to/shriekdj/python-venv-or-virtualenv-wont-activate-on-windows-3e2
Разрешить подобные операции для текущего пользователя
```bash
Set-ExecutionPolicy Unrestricted -Force -Scope CurrentUser
```

Деактивировать в ubuntu: `deactivate`

# UV
uv - более производительный и удобный инструмент для работы с виртуальными окружениями

```
uv venv
uv venv my-name
uv venv --python 3.11

uv pip install package_name
```

todo:

# Pigar

```bash
pip install pigar  # пакет для анализа исходников (.py, .ipynb) для поиска зависимостей

# из корня проекта вызвать:
pigar generate
```

# Ссылки
https://pypi.org/project/virtualenv/

https://habr.com/ru/post/491916/ -- Создание виртуальных окружений и установка библиотек для Python 3 в IDE PyCharm

Короткая шпаргалка по использованию pip и uv: https://miro.com/app/board/uXjVNQC1rq8=/?share_link_id=938578428749