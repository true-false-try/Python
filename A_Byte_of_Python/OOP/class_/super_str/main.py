"""
Разработать класс SuperStr, который наследует функциональность стандартного типа str и содержит 2 новых метода:

метод is_repeatance (s), который принимает 1 аргумент s и возвращает True или False в зависимости от того,
может ли текущая строку быть получена целым количеством повторов строки s.
Вернуть False, если s не является строкой. Считать, что пустая строка не содержит повторов.

метод is_palindrom (), который возвращает True или False в зависимости от того, является ли строка палиндромом.
Регистрами символов пренебрегать. Пустую строку считать палиндромом.
"""


class SuperStr(str):

    def __init__(self, string):
        super().__init__()
        self.string = string

    def is_repeatance(self, s):
        self.s = s
        if type(s) != str:
            return False
        count = self.string.count(s)
        if len(self.string) == len(s) * count:
            return True
        else:
            return False


if __name__ == '__main__':
    s = SuperStr('123123123123')

    print(s.is_repeatance('123'))  # True
    print(s.is_repeatance('12312'))  # False
    print(s.is_repeatance(123))  # False
    print(s.is_repeatance('123123123123'))  # False
