"""
Заданий вектор ГР розмірності n, компонентами якого є записи,що містять анкети службовців деякого закладу.
В кожній анкеті вказується прізвище службовця, його стать, дата народження у вигляді: число, місяць, рік.
Скласти програму пошуку:
а) найстаршого з чоловіків групи ГР;
б) людей з групи ГР, прізвища яких починаються з заданої літери.

"""
import datetime as dt
import random as rm

# creating random data
data = []
for i in range(20):
    day, month, year = rm.randint(1, 29), rm.randint(1, 12), rm.randint(1973, 2000)
    str_day, str_month, str_year = str(day), str(month), str(year)

    # this part add on the front 0 if values <= 9
    if day <= 9 or month <= 9:
        if day <= 9 and month >= 9:
            str_day = '0' + str(day)
        elif day >= 9 and month <= 9:
            str_month = '0' + str(month)
        elif day <= 9 and month <= 9:
            str_day, str_month,  = '0' + str(day), '0' + str(month)

    lst_data = [str_day, str_day, str_year]
    join_data_str = '.'.join(lst_data)
    data.append(join_data_str)

# creating tuple questionnaires_people
questionnaires_people = tuple((['Haloncin', 'man', data[rm.randint(0, 19)]],
                               ['Formalova', 'woman', data[rm.randint(0, 19)]],
                               ['Alenina', 'woman', data[rm.randint(0, 19)]],
                               ['Lavova', 'woman', data[rm.randint(0, 19)]],
                               ['Sabrinova', 'woman', data[rm.randint(0, 19)]],
                               ['Salinof', 'man', data[rm.randint(0, 19)]],
                               ['Velyan', 'man', data[rm.randint(0, 19)]]))

# find old man from tuple questionnaires_people
lst_int_year = []
for i in range(len(questionnaires_people)):
    year_int = int(questionnaires_people[i][2][6:])
    lst_int_year.append(year_int)
print('To the senior employee', dt.datetime.now().year - min(lst_int_year), 'years old')

# find last names that start with the letter you are about to enter
char = str(input("Please, enter one char in range (a-z) or in range (A-Z):")).upper()
print(*[questionnaires_people[i] for i in range(len(questionnaires_people)) if questionnaires_people[i][0][0] == char])
