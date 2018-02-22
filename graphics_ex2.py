# Простая анимация


from graphics import *
from time import sleep



win = GraphWin("My Circle", 100, 100)

i = 0
while True:

	# удалим все объекты из окна
	for item in win.items:
		item.undraw()

	# создадим новую окружность
	c = Circle(Point(50,50), i)

	# нарисуем окружность на окне
	c.draw(win)

	# приостановим программу на 1/30 секунды
	sleep(1/30)
	i = (i+1) % 50
	