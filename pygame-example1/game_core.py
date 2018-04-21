from random import randint

# ширина и высота игрового мира
width = 640
height = 480

# единичный вектор задающий направление движения
UP =     complex( 0, -1)
RIGHT =  complex( 1,  0)
DOWN =   complex( 0,  1)
LEFT =   complex(-1,  0)


# ускорение свободного падения
g = 10


# игровой объект
class GameObject:
    # координаты центра
    coord = complex(0,0)

    w = 10  # ширина
    h = 10  # высота

    # текущая скорость объекта
    v = complex(0,0)

    # максимально возможная скорость
    # вдоль любой из осей
    Speed = 10

    def __init__(self, x=0.0, y=0.0, w=10, h=10):
        self.coord = complex(x,y)
        self.w = w
        self.h = h

    def stop(self):
        self.v = complex(0, 0)

    def set_dir(self, dir):
        """
        :param dir:  complex - единичный двумерный вектор задающий направление движения.
        :return:
        """
        self.v = self.Speed * dir

    def move(self):
        self.coord = self.coord + self.v


# игрок
player = None


obstacles = []

"""
Можно не создавать отдельную функцию, а написать код непостредственно в модуле,
как буд-то это основной модуль. Этот код выполнится при подключении модуля.

Однако лучше иметь возможность заново инициалищировать все переменные в любой момент времени.
"""


def init():
    global player, obstacles
    obstacles = create_obstacles(4)
    player = GameObject(x=width / 2, y=height / 2, w=20, h=20)


def create_obstacles(n):
    obs = []
    w = width/16
    h = height/8

    dx = width/n
    for i in range(n):
        # нижние препятствия
        o1 = GameObject( int(i *dx) - w/2, h/2, w, h*randint(1,4))
        o1.v = complex(-o1.Speed,0)

        # верхние препятствия
        hh = h * randint(1, 4)
        o2 = GameObject(int(i * dx) - w / 2, height - hh / 2, w, hh)
        o2.v = complex(-o2.Speed,0)

        obs += [o1, o2]
    return obs


def is_collision(o1, o2):
    """
    :param o1:
    :param o2:
    :return: True, если два обекта столкнулисб
    """
    return False


def is_boundary_collision(o):
    """
    :param o:
    :return: True если объкт столкнулся с границами экрана
    """
    return False


def gravity(o):
    y  = o.coord.imag
    vy = o.v.real

    # используем формуля для равносукоренного движения
    # y1  = y + Vy * t + g/2 * t^2
    # Vy1 = Vy + g * t
    # t = 1

    y1  = y + vy + g/2
    vy1 =     vy + g

    o.coord = complex ( o.coord.real, y1 )
    o.v = complex(o.v.real, vy1)


# выполнение основных игровых действий
def handle_game():
    global player, obstacles
    player.move()
    gravity(player)

    for obs in obstacles:
        obs.move()
        if obs.coord.real < 0:
            obs.coord = complex(width, obs.coord.imag)

        if is_collision(player, obs) or is_boundary_collision(player):
            # игрок столкнулся с препятствием или с границами экрана
            pass
