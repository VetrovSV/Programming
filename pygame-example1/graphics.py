import pygame

COLOR_OBS = (0, 255, 0)
COLOR_PL = (255,255,0)

# спрайт для игрока
BirdImg = None


def draw_obstacle(scr, obs):
    for o in obs:
        rect = (o.coord.real - o.w / 2, o.coord.imag - o.h / 2, o.w, o.h)
        pygame.draw.rect(scr, COLOR_OBS, rect)



# отрисовка всего
def draw_all(scr, pl, obs ):
    """
    :param pl: игрок
    :return:
    """
    scr.blit(BirdImg, (pl.coord.real - pl.w / 2, pl.coord.imag - pl.h / 2))

    draw_obstacle(scr, obs)


def init():
    global BirdImg
    BirdImg = pygame.image.load("bird.png")

