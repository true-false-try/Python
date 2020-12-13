"""
Дано натуральне число n та послідовність натуральних чисел a1, a2,
…, an. Показати всі елементи послідовності, які є
а) повними квадратами;
б) степенями п’ятірки;
в) простими числами.
Визначити відповідні функції для перевірки, чи є число: повним квадратом,
степенню п’ятірки, простим числом.

"""
import random as rn

n = int(input('Write one number for create a length list:'))

lst_step = [rn.randint(1, 11) for i in range(1, n + 1)]

square_number = list(filter(lambda x: (x ** 0.5).is_integer() == True, lst_step))

fifth_power = list(filter(lambda x: (x ** 0.2).is_integer() == True, lst_step))

# this function shows simple numbers
def simple_number():
    lst_simple = []
    count = 0
    for i in range(len(lst_step)):
        for j in range(2, lst_step[i] + 1):
            if lst_step[i] % j == 0:
                count += 1
        if count == 1:
            lst_simple.append(lst_step[i])
        else:
            count = 0
            continue
        count = 0
    return lst_simple


print('This is list with random numbers:', lst_step, sep='\n')
print('This is a list of square numbers:', square_number, sep='\n')
print('This is a list of fifth power numbers:', fifth_power, sep='\n')
print('This is a list of simple numbers:', simple_number(), sep='\n')
