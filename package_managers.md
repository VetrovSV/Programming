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

# Pyproject.toml
`pyproject.toml` — это главный файл конфигурации Python-проекта. Обычно описывают:
- метаданные проекта: имя, версия, описание, авторы;
- зависимости проекта (необходимые библиотеки);
- пути к папкам с исходными файлами для удобного импорта;
- инструменты сборки и упаковки;
- настройки форматтеров, линтеров, тестов и других утилит.

Сегодня этот файл считается стандартным и самым удобным способом описывать проект в современном Python

`pyproject.toml` заменяет requirements.txt, но позволяет хранить больше информации о проекте и отдельные варианты зависимостей (например для тестов и основной версии проекта).


pyproject.toml поддерживается pip, uv, pixi и другими инструментами.

**Создание pyproject.toml**

Создавать фал можно вручную или с помощью менеджеров проектов, например `uv`:
```bash
uv init [project_name]
```

**Типичный минимальный вариант**
```toml
# описание системы сборки
[build-system]
requires = ["setuptools>=61", "wheel"]
build-backend = "setuptools.build_meta"

# описание проекта
[project]
name = "my_project"                 # название проекта
version = "0.1.0"
description = "Пример проекта"      # описание (не обязательно)
requires-python = ">=3.10"          # требования к версии питона
```

### Синтаксис toml файлов
pyproject.toml написан на языке TOML.

- Файл читается как набор ***[разделов]***. Их имена обычно стандартизированы
- Раздел начинается с заголовка в квадратных скобках, например `[project]`
- Разделы могут быть вложенными, они разделяются точкой: `[main_section.subsection]` 
- Раздел содержит **пары**: ключ = значение.
- Поддерживаются списки, похожие на python-списки, например: `dependencies = ["numpy", "pandas"]`
- В pyproject есть специальные ключи (имена) для списков, например `dependencies`
- Комментарии начинаются с `#`.


### Основные элементы pyproject.toml
Разделы
- `[build-system]` — Нужен для сборки пакета, который является вашим проектом.
  Ключи раздела:
  - `requires` — что нужно для сборки;
  - `build-backend` — кто именно собирает проект.
- `[project]` — основной стандартный раздел с данными о проекте
  - `name`
  - `version`
  - `description`
  - `requires-python`
  - `dependencies` -- список основных зависимостей, заменяет собой отдельный файл requirements.txt
  - `optional-dependencies`
  - `authors`
  - `readme`
  - `license`
- Подраздел `[project.optional-dependencies]` -- дополнительные зависимости. Обычно нужны, чтобы быстро настроить среду для тестов или зависимости, которые нужны не всем. Содержит списки с произвольным именем. Список -- именованный перечень отдельных зависимостей. Пример:  
  ```toml
  [project.optional-dependencies]
  dev = ["pytest", "ruff"]   # зависимости, нужные только во время разработки, не не использования проета
  ml = ["numpy", "pandas", "scikit-learn"]
    ```
- Раздел `[dependency-groups]` -- используется некоторыми современными инструментами для групп зависимостей, например uv


### Пример pyproject
```toml
# описание системы сборки. Обычно не требуется менять
[build-system]
requires = ["setuptools>=61", "wheel"]
build-backend = "setuptools.build_meta"

# описание проекта -- самая важная часть
[project]
name = "my_project"
version = "0.1.0"
description = "Учебный проект"
requires-python = ">=3.10"
dependencies = ["requests", "numpy"]

# дополнительные зависимости
[project.optional-dependencies]
dev = ["pytest", "ruff"]
```


### Работа с файлом

**Установка зависимостей**

Выполнить команду в корне проекта, где находится `pyproject.toml`
```bash
pip install .
```

Если нужен режим разработки, когда изменения в коде подхватываются без переустановки, используют editable-install
```bash
pip install -e .
```


**Установить дополнительные зависимости**

```bash
pip install ".[dev]"
pip install ".[ml]"
```

Или с помощью `uv`

```bash
# конкретный набор доп зависимостей
uv sync --extra dev
# все зависимости
uv sync --all-extras
```


### Пример работы через `uv`

```bash
# создать новый проект
uv init my_project

# добавить зависимость
uv add requests

# добавить dev-зависимость
uv add --dev pytest

# добавить optional dependency
uv add httpx --optional network

# убрать зависимость
uv remove requests

# синхронизировать окружение
uv sync

# посмотреть дерево зависимостей
uv tree

# собрать пакет
uv build
```


### Пример работы через `pixi`
```bash
# установить/синхронизировать окружение
pixi install

# запустить команду в окружении
pixi run python

# добавить зависимость
pixi add --pypi boto3

# добавить зависимость в feature
pixi add --pypi boto3 --feature aws

# удалить зависимость
pixi remove --pypi boto3
```
