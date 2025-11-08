"""
server_litestar.py

Простой HTTP API на Litestar — аналог вашего примера hello_world на FastAPI.
LiteStar быстрее чем FastAPI
granian - более быстрый чем uvicorn веб-сервер.
Без учёта задержки выполнения кода, вызванного в обработчиках LiteStar прирост скорости в стеке granian + litestar по сравнению с uvicorn + FastAPI может быть в несколько раз. 

granian --interface asgi --workers 16 main:app
"""

from random import randint
from typing import Dict
from litestar import Litestar, get


@get("/")
async def root() -> Dict[str, str]:
    """health-check; в норме выдаёт {"status": "Ok"}"""
    return {"status": "Ok"}


@get("/number")
async def number() -> Dict[str, int]:
    """Выдаёт случайное число от 0 до 100 включительно"""
    return {"number": randint(0, 100)}


@get("/number_with_params")
async def number_with_params(min: int, max: int) -> Dict[str, int]:
    """
    Выдаёт случайное число от min до max включительно.
    Если min > max — автоматически переставляем границы.
    (Так мы избегаем ошибки и не возвращаем 500.)
    """
    lo, hi = (min, max) if min <= max else (max, min)
    return {"number": randint(lo, hi)}


# Создаём приложение Litestar из обработчиков
app = Litestar(route_handlers=[root, number, number_with_params])
