# Инструменты для работы с кодом и зависимостями

Пакетные менеджеры:
* Pip — пакетный менеджер, входит в дистрибутив python;
* pip-tools — надстройка над pip для компиляции зависимостей.
* Poetry — для сложных зависимостей и публикации пакетов.
* uv — для современных проектов, где важны скорость и простота. Подходит для замены pip, virtualenv и pyenv 135.
* Conda — для научных задач с не-Python зависимостями.


# UV
Современный инструмент на Rust, позиционируется как замена pip, pip-tools, virtualenv и pyenv.

* В 10–100 раз быстрее pip благодаря кэшированию и оптимизациям
* Управление версиями Python: Команды uv python install и uv python pin позволяют устанавливать и переключать версии интерпретатора
* Интеграция с существующими workflow: Поддерживает requirements.txt, создание виртуальных окружений через uv venv, а также инструменты вроде uvx для запуска утилит (например, uvx black) во временных окружениях

https://docs.astral.sh/uv/getting-started/

#### Устанвока

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh  # Linux/macOS

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Или через pip:
pip install uv
```

### Использование

#### Пакеты

```bash
uv pip install [пакет]           # Установить пакет (как pip)
uv pip install -r requirements.txt  # Установить зависимости из файла
uv pip freeze > requirements.txt    # Экспорт зависимостей
uv pip compile requirements.in -o requirements.txt  # Генерация lock-файла
```

#### lock файлы
Совместно с requirements.txt используются lock файлы. Они фиксируют неуказанные в requirements пакеты. 

Например в requirements.txt указано:
```
requests>=2.25.0
```

Без lock-файла при установке может скачаться requests 2.31.0, а с ним — несовместимая версия urllib3.

Lock-файл фиксирует точные версии:
```
requests==2.31.0
urllib3==2.0.7  # автоматически добавленная зависимость
```

#### Виртуальные окружения**
```bash
uv venv .venv                     # Создать окружение в папке .venv
source .venv/bin/activate         # Активировать (Linux/macOS)
.venv\Scripts\activate            # Активировать (Windows)
```