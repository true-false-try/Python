"""
Объявите класс Point с конструктором, который бы позволял создавать экземпляр на основе другого, уже существующего.
Если аргументы в конструктор не передаются, то создаеться объект с локальными атрибутами по умолчанию.
"""


class Point:

    def __init__(self, x_or_object=None, y=None):

        if isinstance(x_or_object, Point):
            self.x = x_or_object
            self.y = y

        else:
            self.x = x_or_object
            self.y = y


if __name__ == '__main__':
    p1 = Point(10, 20)
    p2 = Point()
    print(type(p2))
    print(p2.__dict__)
