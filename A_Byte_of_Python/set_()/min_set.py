"""
Скласти програму, що визначає мінімальний елемент числової
множини.

"""
import random as rn

s = set()
n = int(input('Enter number: '))

for i in range(n):
    s.add(rn.randint(1, 10_000))

print(*s)
print('min value : ', min(s))

