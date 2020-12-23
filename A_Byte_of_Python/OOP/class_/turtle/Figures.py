import turtle
import random


class Point:
    """Точка екрану
    """
    _count = 0

    def __init__(self, x, y):
        self._x = x  # _x - координата x точки
        self._y = y  # _y - координата y точки
        self._visible = False  # _visible - чи є точка видимою на екрані
        Point._count += 1

    def getx(self):
        """Повертає координату x точки
        """
        return self._x

    def gety(self):
        """Повертає координату y точки
        """
        return self._y

    def onscreen(self):
        """Перевіряє, чи є точка видимою на екрані
        """
        return self._visible

    def switchon(self):
        """Робить точку видимою на екрані
        """
        if not self._visible:
            self._visible = True
            turtle.up()
            turtle.setpos(self._x, self._y)
            turtle.down()
            turtle.dot()

    def switchoff(self):
        """Робить точку невидимою на екрані
        """
        if self._visible:
            self._visible = False
            turtle.up()
            turtle.setpos(self._x, self._y)
            turtle.down()
            turtle.dot(turtle.bgcolor())

    def move(self, dx, dy):
        """Пересуває точку на екрані на dx, dy позицій
        """
        vis = self._visible
        if vis:
            self.switchoff()
            self._x += dx
            self._y += dy
        if vis:
            self.switchon()

    def printcount():
        print('Кількість точок:', Point._count)
    printcount = staticmethod(printcount)


class Rectangle(Point):

    def __init__(self, x, y, long, height):
        Point.__init__(self, x, y)
        self._long = long
        self._height = height

    def get_long(self):
        return self._long

    def get_height(self):
        return self._height

    def switchon(self):
        if not self._visible:
            self._visible = True
            turtle.up()
            turtle.setpos(self._x, self._y - (self._long - self._height))
            turtle.down()
            count = 1
            for i in range(4):
                if count % 2 == 1:
                    turtle.forward(self._long)
                    turtle.right(90)
                    count += 1
                else:
                    turtle.forward(self._height)
                    turtle.right(90)
                    count += 1

    def switchoff(self):
        if self._visible:
            self._visible = False
            turtle.down()
            col = turtle.pencolor()
            turtle.pencolor(turtle.bgcolor())
            count = 1
            for i in range(4):
                if count % 2 == 1:
                    turtle.forward(self._long)
                    turtle.right(90)
                    count += 1
                else:
                    turtle.forward(self.get_height())
                    turtle.right(90)
                    count += 1
            turtle.pencolor(col)


if __name__ == '__main__':
    how = int(input('Скількі вивести прямокутників? '))
    window = turtle.Screen()
    window.setup(900, 700)
    pause = 50
    turtle.home()
    turtle.delay(pause)
    p = Point(-20, 10)
    p.switchon()
    p.move(20, 20)
    c = Rectangle(10, 0, 30, 60)
    turtle.speed(30)

    lst_color = ['red', 'blue', 'green', 'pink', 'brown', 'yellow']
    for i in range(how):
        c.switchon()
        turtle.pencolor(lst_color[i % random.randint(1, 6)])
        if i % 2 == 1:
            c.move(random.randint(50, 200), random.uniform(100, 50))
        c.move(random.randint(-100, -1), random.uniform(-1, -100))



