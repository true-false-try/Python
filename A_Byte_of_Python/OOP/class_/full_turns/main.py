"""
Дан список, состоящий из произвольного числа направлений поворотов («left» и/или «right»).
Напишите функцию, которая будет принимать этот список и определять, сколько полных оборотов сделано.

Примечания
Каждый поворот влево или вправо считается поворотом на 90 градусов.
Один оборот = 360 градусов в одном направлении.
Вернуть надо положительное число.
"""


class Around:

    def __init__(self, lst):
        self.lst = list(lst)

    def count_turn(self):
        d_left = self.lst.count('left') * 90
        d_right = self.lst.count('right') * 90
        total = abs(d_left - d_right) // 360
        print(total)


if __name__ == '__main__':
    spin_around = Around(["left", "right", "left", "right"])
    spin_around.count_turn()

    spin_around = Around(["right", "right", "right", "right", "right", "right", "right", "right"])
    spin_around.count_turn()

    spin_around = Around(["left", "left", "left", "left"])
    spin_around.count_turn()

