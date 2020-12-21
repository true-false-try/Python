class Person:
    def __init__(self, name, byear):
        self.name = name
        self.byear = byear

    def input(self):
        self.name = input('Прізвище: ')
        self.byear = input('Рік народження: ')

    def print(self):
        print(self.name, self.byear, end=' ')


