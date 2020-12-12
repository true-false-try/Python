"""
Два пpостих числа називаються "близнюками", якщо вони
відpізняються один від одного на 2 (напpиклад, числа 41 та 43). Скласти
програму виведення на друк всіх паp "близнюків" з відpізку [n,2*n], де n -
задане ціле число, яке більше 2.

"""

n = int(input('Enter values more then 2: '))

while n < 3:
    n = int(input('This value not more then 2,'
                  'enter values more then 2: '))

# create list with range [n, n * 2]
lst_step = [i for i in range(n, (n * 2) + 1)]

if n % 2 == 0:
    twins = list(filter(lambda step: step % 2 == 0, lst_step))
else:
    twins = list(filter(lambda step: step % 2 == 1, lst_step))

# output list twins
print(twins)
