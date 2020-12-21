from A_Byte_of_Python.OOP.class_.employee.Person import *
import shelve
import random


class Employee(Person):

    def __index__(self, tab_num, salary):
        super().input()
        self.tab_num = tab_num
        self.salary = salary

    # this function add a new person in report_card
    def add_employee(self):
        file = shelve.open('report_card')
        with file as card:
            super().input()
            self.tab_num = input('Табельний номер: ')
            self.salary = input('Заробітна платня: ')
            card[self.tab_num] = self.name, self.byear, self.salary
            file.close()

    # this function calculates the actual salary of each person in report_card for working hours
    def salary_month(self):
        # hours per month
        month = 168
        file = shelve.open('report_card')
        # counting the number of people in report_card
        count_ppl = sum([1 for i in file])

        for i in range(1, count_ppl + 1):
            # random value of how many hours a person worked in month
            worked_out = random.randint(1, 168)
            # calculation of actual earnings for hours worked
            fact_salary = (int(file[str(i)][2]) * worked_out) / month

            print('Співробітник:', file[str(i)][0],
                  'Зарплата за 168 год в місяць:', file[str(i)][2],
                  'Відпрацьовано годин: ', worked_out,
                  'Фактична зарплата:', round(fact_salary, 2), sep='\n')
            print()
        file.close()


empl = Employee(name=None, byear=None)

#empl.add_employee()
empl.salary_month()
