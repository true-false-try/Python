"""
Создайте словарь, связав его с переменной school, и наполните данными,
которые бы отражали количество учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т. п.).
Внесите изменения в словарь согласно следующему:
a) в одном из классов изменилось количество учащихся,
b) в школе появился новый класс,
c) в школе был расформирован (удален) другой класс. Вычислите общее количество учащихся в школе.

"""

school = {'1a': 23, '1b': 21, '2a': 18,
          '2c': 24, '2b': 20, '3a': 26,
          '4a': 17, '4b': 16, '4c': 18}

# a) recreate
school.update({'2c': 21})
print(school['2c'])

# b) create a new class
school.setdefault('3b', 12)


# c) del class
del school['1b']

# find count people who learn this school
total_people = sum([school[i] for i in school])
print(total_people)




