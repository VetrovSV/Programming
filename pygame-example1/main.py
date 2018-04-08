import pygame
from pygame import *

import graphics
import game_core


# ширина и высота окна
W,H = 640, 480


def key_handle(events):
    key = None
    for e in events:  # Обрабатываем события
        # обработка события - закрытие окна
        if e.type == QUIT: raise SystemExit("QUIT")

        # обработка нажатия клавиш
        if e.type == pygame.KEYDOWN:

            # выход по нажатия на клавишу esc
            if e.key == pygame.K_ESCAPE: raise SystemExit("QUIT")

    return pygame.key.get_pressed()


def act_player(pl, key):
    if key[pygame.K_UP]:
        pl.set_dir(game_core.UP)
    elif key[pygame.K_RIGHT]:
        pl.set_dir(game_core.RIGHT)
    elif key[pygame.K_DOWN]:
        pl.set_dir(game_core.DOWN)
    elif key[pygame.K_LEFT]:
        pl.set_dir(game_core.LEFT)
    else:
        pl.stop()


pygame.init()  # Инициация PyGame
screen = pygame.display.set_mode((W, H))  # Создаем окно

# Создание видимой поверхности (поверхности для рисования)
bg = Surface((game_core.width, game_core.height))

# Заливаем поверхность сплошным цветом
bg.fill(Color(0,0,0))

# нажатая в данным момент клавиша
key = None
pygame.key.set_repeat(0,50)

while True:
    screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать

    key = key_handle(pygame.event.get())

    act_player(game_core.player, key)
    game_core.handle_game()
    graphics.draw_all(screen, game_core.player)

    pygame.display.update()  # обновление и вывод всех изменений на экран
