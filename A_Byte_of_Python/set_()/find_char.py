"""
Дано рядок з малих латинських літер.
Надрукувати:
a) перші входження літер до рядка, зберігаючи початковий взаємний порядок;
b) всі літери,що входять до рядка не менше двох раз в порядку збіьшення (a - z);
c) всі літери, що входять до рядка по одному разу

"""
string = 'abc abs sda faj'
words = string.split()
together = ''.join(words)
list_couple, list_one, list_first_letter = [], [], []


# a)
def first_letter():
    for i in together:
        for j in range(97, 123):
            if chr(j) == i and i not in list_first_letter:
                list_first_letter.append(chr(j))
    return list_first_letter


# b) and c)
def couple_and_one():
    for i in range(97, 123):
        count = 0
        for j in together:
            if chr(i) == j:
                count += 1
            if count >= 2:
                list_couple.append(chr(i))
        if count == 1:
            list_one.append(chr(i))
    return 'Letters that occur at least 2 times:', \
           sorted(list(set(list_couple))), \
           'Letters that occur once:', list_one


print('The first occurrence of letters in a line:', first_letter(), sep='\n')
print(*couple_and_one(), sep='\n')
