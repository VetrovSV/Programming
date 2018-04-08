# ширина и высота игрового мира
width = 640
height = 480

# единичный вектор задающий направление движения
UP =     complex( 0, -1)
RIGHT =  complex( 1,  0)
DOWN =   complex( 0,  1)
LEFT =   complex(-1,  0)


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
    Speed = 1

    def __init__(self, x=0.0, y=0.0, w=10, h=10):
        self.coord = complex(x,y)
        self.w = w
        self.h = h

    def stop(self):
        self.v = complex(0, 0)

    def set_dir(self, dir):
        self.v = self.Speed * dir

    def move(self):
        self.coord = self.coord + self.v


# игрок
player = GameObject(x = width/2, y = height/2, w = 20, h = 20)


# выполнение основных игровых действий
def handle_game():
    player.move()

