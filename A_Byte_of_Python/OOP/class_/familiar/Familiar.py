from A_Byte_of_Python.OOP.class_.familiar.Person import *


class Familiars(Person):

    def __init__(self, name, byear, tel):
        super().__init__(name, byear)
        self.tel = tel

    def input(self):
        super().input()
        self.tel = input('Номер телефону: ')

    def print(self):
        super().print()
        print(self.tel, end=' ')

    def add_phonebook(self):
        super().input()
        self.tel = input('Номер телефону: ')
        file = open('phonebook.txt', 'a', encoding='utf-8')
        str_famil = self.name + " " + self.byear + " " + self.tel
        file.write(str_famil + '\n')
        file.close()

    def find_tell(self):
        name = input("Прізвище: ")
        file = open('phonebook.txt', 'r', encoding='utf-8')
        lst_famil = [i.rstrip().split() for i in file]
        file.close()
        return [lst_famil[i][2] for i in range(len(lst_famil) - 1)
                if lst_famil[i][0].lower() == name.lower()]


std1 = Familiars(name=None, byear=None, tel=None)

# output
# std1.input()
# std1.print()
# std1.add_phonebook()
#print(*std1.find_tell())

