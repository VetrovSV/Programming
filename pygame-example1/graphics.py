import pygame


# отрисовка всего
def draw_all(scr, pl ):
    """
    :param pl: игрок
    :return:
    """
    plrect = ( pl.coord.real - pl.w/2, pl.coord.imag - pl.h/2,  pl.w, pl.h)
    pygame.draw.rect(scr, (255,255,0), plrect)




