# Менеджеры контекста

**Менеджер контекста** — объект, который обеспечивает корректный захват и освобождение ресурса вокруг блока кода, указываемого через `with ...:`. Позволяет гарантировать очистку (закрытие файлов, откат транзакций, освобождение блокировок и т.п.) даже при ошибках.

Синтаксис:

```py
with <context_expr> as <var>:
    # блок, где ресурс доступен как var
```

## Когда использовать

- Работа с ресурсами: файлы, сетевые соединения, сокеты, блокировки, транзакции БД, временные директории/файлы.
- Временные изменения окружения (смена cwd, изменение логгера, redirect stdout).
- Гарантированное измерение времени/логирование начала/конца операций.

## Когда не использовать

- Для простых локальных операций, где достаточно явного вызова `open/close` если код выполняется в одном месте и очень простой.
- Когда управление ресурсом передаётся далеко и сложными цепочками (тогда лучше явные объекты с явными методами `.close()` и надежный контракт).

## Как работает

Менеджер контекста реализует протокол с методами:

- `__enter__(self)` — вызывается при входе; может вернуть ресурс, который присваивается после `as`.
- `__exit__(self, exc_type, exc, tb)` — вызывается при выходе из блока. Аргументы описывают возникшее исключение (или `None, None, None`).
  - Если `__exit__` вернёт `True`, исключение будет подавлено (не проброшено дальше). Обычно возвращают `False` (или ничего), чтобы исключения шли дальше.

Таким образом, класс, экземпляр которого создаётся в `context_expr` должен реализовывать эти два метода.

Обработки исключений:

- Если исключение возникает **внутри** блока `with`, `__exit__` всё равно вызывается.
- Если исключение происходит в `__enter__`, то `__exit__` **не** вызывается.

Альтернативный способ — декоратор `@contextlib.contextmanager`, который позволяет описать менеджер как генератор: код до `yield` — вход, `yield` отдаёт значение в `as`, код после `yield` — очистка (вызывается и при исключении).

## Примеры использвания

### Файлы

```py
# Чтение
with open('data.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Запись (атоматическое создание/перезапись)
with open('out.txt', 'w', encoding='utf-8') as f:
    f.write('hello\n')

# Бинарный режим и поблочная запись
with open('image.jpg', 'rb') as r, open('copy.jpg', 'wb') as w:
    while chunk := r.read(8192):
        w.write(chunk)
```

### Работа с СУБД

```py
import sqlite3

with sqlite3.connect('db.sqlite3') as conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS t (id INTEGER PRIMARY KEY, v TEXT)')
    cur.execute('INSERT INTO t(v) VALUES (?)', ('hello',))
# commit/rollback выполнятся автоматически
```

### Критические секции в паралельных алгоритмах

```py
import threading

lock = threading.Lock()
with lock:
    # критическая секция
    do_critical_work()
```

### HTTP запросы

```py
import requests

url = 'https://example.com/large-file'

# Session автоматически закроется
with requests.Session() as s:
    r = s.get(url, timeout=10)
    r.raise_for_status()
    data = r.text

# Streaming (закрывает ответ по выходу из with)
with requests.Session() as s:
    with s.get(url, stream=True, timeout=10) as r:
        r.raise_for_status()
        for chunk in r.iter_content(8192):
            process(chunk)
```

`requests.Session()` — это объект сессии , который:

- Переиспользует TCP-соединения (connection pooling).
- Хранит общие настройки для серии запросов:
  - cookies
  - headers
  - auth
  - proxies
  - параметры по умолчанию

Рекомендуется использовать когда нужно выполнить множестов запросов.

### Асинхронные HTTP запросы

```py
import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=10) as resp:
            return await resp.text()

asyncio.run(fetch('https://example.com'))
```

## Пример реализация

```py
class MyRes:
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        print('acquire', self.name)
        return self  # доступный объект
    def __exit__(self, exc_type, exc, tb):
        print('release', self.name)
        # вернуть True, если хотим подавить исключение
```

Использование:

```py
with MyRes('r') as r:
    pass
```

### Менеджер через contextlib

```py
from contextlib import contextmanager

@contextmanager
def managed(name):
    print('acquire', name)
    try:
        yield name
    finally:
        print('release', name)
```

with managed('r') as r:
pass

````

## Полезные примеры
### Открытие файла (стандартный паттерн)
```py
with open('data.txt', 'r', encoding='utf-8') as f:
    text = f.read()
# файл закрыт автоматически
````

### Блокировка

```py
import threading
lock = threading.Lock()
with lock:
    # критическая секция
    pass
```

### Транзакция (пример шаблона)

```py
class Transaction:
    def __init__(self, conn):
        self.conn = conn
    def __enter__(self):
        self.conn.begin()
        return self.conn
    def __exit__(self, exc_type, exc, tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
            # не подавляем исключение — возвращаем False
```

### Временная смена рабочей директории

```py
from contextlib import contextmanager
import os

@contextmanager
def chdir(path):
    old = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old)
```

### Подавление конкретных исключений

```py
from contextlib import suppress
from pathlib import Path

with suppress(FileNotFoundError):
    Path('nope.txt').unlink()
# если файла нет — исключение не поднимется
```

### ExitStack — динамическое число менеджеров

```py
from contextlib import ExitStack

files = ['a.txt', 'b.txt', 'c.txt']
with ExitStack() as stack:
    handles = [stack.enter_context(open(fn)) for fn in files]
    # все файлы будут закрыты при выходе
```

## Лучшие практики

- Используйте `with` для любых ресурсов, которые требуют освобождения.
- В `__exit__` не подавляйте исключения по умолчанию; подавляйте **только** если вы уверены, что это безопасно.
- Делайте `__enter__` максимально простоым. Лучше только получить ресурс, а сложную инициализацию можно выполнить отдельно.
- Если в `__enter__` выделяется ресурс, будьте уверены, что в случае ошибки ничего не останется неуправляемым (используйте идиому выделения внутри `try/except` или доверяйте `contextmanager`-генератору).
- Используйте `ExitStack` для динамических/условных ресурсов.
- Документируйте поведение при исключениях и явно указывайте, подавляет менеджер ошибки или нет.
- Для тестов пишите простые контекст-менеджеры (mock), чтобы контролировать время/локи/файлы.
- Отделяйте логику приобретения ресурса от логики обработки — это улучшает тестируемость.

## Частые ошибки и подводные камни

- **Ожидание вызова `__exit__` при ошибке в `__enter__`.** Если `__enter__` выбросил — `__exit__` не вызывается.
- **Подавление исключений необдуманно**. Если `__exit__` возвращает `True`, ошибка пропадает — это может скрыть баги.
- **Долгая/блокирующая работа в `__enter__`** (например, сетевые запросы) — усложняет тестирование и поведение при исключениях.
- **Изменение внешнего состояния без восстановления** — всегда делайте `finally`/`__exit__` для отката.

## Быстрый референс (стандартные менеджеры)

- `open(...)` — файлы.
- `contextlib.suppress(...)` — подавление исключений.
- `contextlib.redirect_stdout/redirect_stderr` — перенаправление вывода.
- `contextlib.ExitStack` — стек контекстов.
- `contextlib.nullcontext` — пустой менеджер (полезен для условного `with`).
- `tempfile.TemporaryDirectory`, `tempfile.TemporaryFile` — временные ресурсы.
- `contextlib.closing(obj)` — закрывает объект, у которого есть `.close()` (полезно для socket.makefile и др.).
