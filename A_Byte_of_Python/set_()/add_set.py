"""
Визначити функцію доповнення множини, якщо відома
універсальна множина.

"""
import random as rn

s, s1 = set(), {10, 12, 1, 2, 3, 20, 200, 34, 102}
n = int(input('Enter number: '))

for i in range(n):
    s.add(rn.randint(1, 20))
s1.update(s)

print(s1)
