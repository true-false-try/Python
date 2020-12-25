"""
Напишите программу, в которой пользователь вводит координаты x, y с клавиатуры, создается соответсвующий
экземпляр и он сохраняется в списке. Количество вводимых объектов n = 5.
Затем вывести их атрибуты в консоль.
"""


class Program:

    def __init__(self, x, y):
        self.x = x
        self.y = y


lst_vector = []
for i in range(5):
    x = input('Enter x:')
    y = input('Enter y:')
    p = Program(x, y)
    lst_vector.append(p.__dict__.values())
    print(lst_vector)
