"""
Відомості про учня складаються з його унікального номера
учнівського квитка, любий пятизначный номер.
Дано словник, який містить відомості про учнів школи.
Скласти програми, які дозволяють
a) визначити, чи є в школі учні з однаковим прізвищем;
b) визначити, чи є учні з однаковим прізвищем в якихось паралельних класах;
c) визначити, чи є учні з однаковим прізвищем у якомусь класі;
d) визначити, в яких класах нараховується більше. ніж 35 учнів;
e) визначити, на скільки учнів в восьмих класах більше, ніж в десятих;
f) зібрати у словник відомості про учнів 10-х і 11-х класів, помістивши спочатку відомості про учнів класу 10а, потім 10б і т.д.

"""
# create dictionary
dictionary = {32311: ['Yevhenii', 'Chekhovskyi', '11', 'D', 36],
              33312: ['Yana', 'Germosova', '11', 'C', 12],
              31313: ['Olga', 'Kentok', '11', 'B', 23],
              32214: ['Alex', 'Chekhovskyi', '11', 'A', 41],
              32423: ['Alex', 'Chekhovskyi', '11', 'C', 31],
              23415: ['Alex', 'Chekhovskyi', '11', 'E', 30],
              33315: ['Kate', 'Loboda', '8', 'A', 20],
              22316: ['Sveta', 'Loboda', '8', 'A', 20],
              32317: ['Alyona', 'Loboda', '7', 'B', 22],
              34318: ['Max', 'Lonchik', '7', 'C', 23],
              52319: ['Slava', 'Krovik', '10', 'B', 20],
              52339: ['Gena', 'Kolpak', '10', 'A', 15]}


# a) this function finding the same last name
def same_last_name():
    print("Students with the same surname is:")
    count = 0
    for i in dictionary:
        for j in dictionary:
            if dictionary[i][1] == dictionary[j][1]:
                count += 1
        if count > 1:
            print(dictionary[i][0], dictionary[i][1], sep=' ')
        count = 0
    print()


# b) this function determine whether there are students with the same last name in any parallel classes
def opposite_class():
    count = 0
    lst_opposite = []
    for i in dictionary:
        for j in dictionary:
            if dictionary[i] != dictionary[j]:
                if dictionary[i][1] == dictionary[j][1] and dictionary[i][2] == dictionary[j][2] and \
                        dictionary[i][2] == dictionary[j][2]:
                    count += 1
        if count > 1:
            lst_opposite.append(dictionary[i])
        count = 0
    print("Students with the same surname and they are opposite class:", *lst_opposite, sep='\n')
    print()


# c) this function determine if there are students with the same last name in a class
def classmates_have_the_same_surname():
    print("Сlassmates with the same surname is:")
    count = 0
    for i in dictionary:
        for j in dictionary:
            if dictionary[i][1] == dictionary[j][1] and dictionary[i][2] == dictionary[j][2]:
                if dictionary[i][3] == dictionary[j][3]:
                    count += 1
        if count > 1:
            print(dictionary[i][0], dictionary[i][1], sep=' ')
        count = 0
    print()


# d) this function determine in which classes there are more, than 35 students
def more_than_35():
    numb_class = [(value[2] + value[3]) for key, value in dictionary.items() if value[4] > 35]
    print('Classes that include more than 35 people:', *numb_class, sep='\n')
    print()


# e) this function determine how many students in the eighth grade are more than in the tenth:
def class_differences():
    difference = sum([int(value[4]) for key, value in dictionary.items() if value[2] == '8']) \
                 - sum([int(value[4]) for key, value in dictionary.items() if value[2] == '10'])
    if difference > 0:
        print('In the eighth grade students are more by', difference)
    elif difference < 0:
        print('In the tenth grade students are more by', abs(difference))
    else:
        print('In the eighth and tenth grades equally students')
    print()


# f) this function creates a new dictionary with sorted data from 10th to 11th grades
def new_dictionary():
    new_dict = {}
    # select all students from 10th to 11th grade and add them to the new_dict
    for key, value in dictionary.items():
        if 10 <= int(value[2]) <= 11:
            new_dict.setdefault(key, value)

    # select from new_dict and sort it by the third and fourth elements
    for i in sorted(new_dict.items(), key=lambda couple: (couple[1][2], couple[1][3])):
        print(i)

# output
same_last_name()
opposite_class()
classmates_have_the_same_surname()
more_than_35()
class_differences()
new_dictionary()
