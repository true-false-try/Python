"""
Заданий вектор розмірності n, компоненти якого містять
інформацію про студентів деякого вузу. Відомості про кожного студента
складаються з указання його прізвища, ім'я, по батькові, статі, віку, курсу.
Скласти програму пошуку
а) найбільш поширених чоловічих та жіночих імен;
б) прізвищ та ініціалів усіх студентів, вік яких є найбільш поширеним.

"""
# create tuple
group_students = tuple((['Alice', 'Yevheniivna', 'Chuckotkina', 'woman', 23, 4],
                        ['Olga', 'Olegovna', 'Kupkina', 'woman', 21, 3],
                        ['Alice', 'Alexandrova', 'Popova', 'woman', 23, 3],
                        ['Alena', 'Olegovna', 'Kupkina', 'woman', 19, 2],
                        ['Olga', 'Kirilovna', 'Kurop', 'woman', 24, 5],
                        ['Andrey', 'Alexeevich', 'Fomin', 'man', 23, 4],
                        ['Alex', 'Alexandrovich', 'Checkhov', 'man', 18, 1],
                        ['Andrey', 'Ivanovich', 'Ivanov', 'man', 18, 2],
                        ['Anton', 'Igilov', 'Checkin', 'man', 18, 1],
                        ['Alex', 'Olegovich', 'Ivanchenko', 'man', 18, 2],
                        ['Andrey', 'Petrovich', 'Petrov', 'man', 17, 1]))


# This function performs the function of item: a)
def find_popular_name():
    # find the most extended man name from group_students
    all_man = [group_students[i] for i in range(len(group_students)) if group_students[i][3] == 'man']

    count_all = 0
    count_max = 0
    lst_with_extend_name = []

    for i in range(len(all_man)):
        for j in range(len(all_man)):
            if all_man[i][0] == all_man[j][0]:
                count_all += 1
        if count_max <= count_all:
            count_max = count_all
            lst_with_extend_name.append(all_man[i][0])
        count_all = 0
    count_max = 0

    # find the most extended woman name from group_students
    all_woman = [group_students[i] for i in range(len(group_students)) if group_students[i][3] == 'woman']

    for i in range(len(all_woman)):
        for j in range(len(all_woman)):
            if all_woman[i][0] == all_woman[j][0]:
                count_all += 1
        if count_max <= count_all:
            count_max = count_all
            lst_with_extend_name.append(all_woman[i][0])
        count_all = 0

    count_lst_with_extend_name = 0

    for i in lst_with_extend_name:
        for j in lst_with_extend_name:
            if i == j:
                count_lst_with_extend_name += 1
        if count_lst_with_extend_name == 1:
            lst_with_extend_name.remove(i)
        count_lst_with_extend_name = 0

    return list(set(lst_with_extend_name))


# This function performs the function of item: b)
def find_popular_age():
    # find popular age from  tuple group_students
    count = 0
    count_max = 0
    popular_age = 0

    for i in range(len(group_students)):
        for j in range(len(group_students)):
            if group_students[i][4] == group_students[j][4]:
                count += 1
                if count > count_max:
                    count_max = count
                    popular_age = group_students[i][4]
        count = 0
    # find the surnames and initials of those people whose age is most common in the tuple group_students
    name_popular_age = [(group_students[i][2],
                         group_students[i][0][0],
                         group_students[i][1][0]) for i in range(len(group_students)) if group_students[i][4] == popular_age]
    print()

    return name_popular_age


# output
print('Most popular names:', *find_popular_name(), sep='\n')
print('Most popular students by age:', *find_popular_age(), sep='\n')




