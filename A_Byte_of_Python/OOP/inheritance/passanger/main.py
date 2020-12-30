from random import randint


class Person:
    def __init__(self):
        self.name = None
        self.byear = None

    def input(self):
        self.name = input('Прізвище: ')
        self.byear = input('Рік народження: ')

    def print(self):
        print(self.name, self.byear, end=' ')


class Passanger(Person):
    def __init__(self):
        Person.__init__(self)
        self.departure_city = None
        self.arrival_city = None
        self.list_person = []
        self.total_list_person = []

    def input(self):
        Person.input(self)
        self.departure_city = input('Місто з якого ви прямуєте: ')
        self.arrival_city = input('Місто куди ви прямуєте: ')
        # noinspection PyAttributeOutsideInit
        self.distance = randint(100, 2001)
        self.list_person.extend((self.departure_city, self.arrival_city, self.distance))

    def print(self):
        print(self.name, self.byear, self.departure_city, self.arrival_city, self.distance)

    def price(self):
        price_1_km = 0.5
        for i in range(len(self.list_person)):
            if i == 2:
                price_ticket = round((self.list_person[i] * price_1_km), 2)
                self.total_list_person.extend([self.name, self.byear, self.departure_city,
                                               self.arrival_city, self.distance, price_ticket])
                print('Price is:', price_ticket)
                self.list_person.clear()


if __name__ == '__main__':
    n = int(input('Введіть скільки пасажірів будуть їхати: '))
    for i in range(n):
        p = Passanger()
        p.input()
        p.print()
        p.price()
    print('List all passanger: ', p.total_list_person, sep='\n')






