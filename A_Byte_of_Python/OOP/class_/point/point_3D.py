"""
Создайте класс Point3D, который хранит координаты в виде списка. Пропишите у него конструктор для создания экземпляров
с локальными координатами. Также добавьте методы, позволяющие изменить координаты и получить их в виде кортежа.
"""


class Point3D:

    def __init__(self, x, y, z):
        self.__vector = []
        self.x = self.__vector.append(x)
        self.y = self.__vector.append(y)
        self.z = self.__vector.append(z)

    def change_vector(self, x, y, z):
        if len(self.__vector) > 0:
            self.__vector.clear()

        self.x = self.__vector.append(x)
        self.y = self.__vector.append(y)
        self.z = self.__vector.append(z)

    def tuple_input(self):
        print(tuple(self.__vector))


if __name__ == '__main__':
    p = Point3D(1, 2, 3)
    p1 = Point3D(10, 20, 30)
    p1.change_vector(5, 100, 200)
    p1.tuple_input()


