"""
Заданий вектор ГР, компонентами якого ГР(х) є записи, що
містять дані про людину з іменем Х із вказаного списку. Кожне дане
складається з вказаної статі людини та її зросту. Скласти програми для
а) обчислення середнього зросту жінок з групи ГР;
б) пошуку найвищого чоловіка;
в) перевірки, чи є в групі ГР дві людини, однакові на зріст.
"""

group_people = tuple((['Alice', 'woman', 172], ['Alex', 'man', 183],
                      ['Alice', 'woman', 172], ['Nicolas', 'man', 193],
                      ['Dasha', 'woman', 163], ['John', 'man', 178]))

#---------- calculation of the average height of women from group_people ---------------------------------
total_woman = sum([group_people[i][2] for i in range(len(group_people)) if group_people[i][1] == 'woman'])
count_woman = sum([1 for i in range(len(group_people)) if group_people[i][1] == 'woman'])

#---------- finding the tallest man ----------------------------------------------------------------------
count_man = sum([1 for i in range(len(group_people)) if group_people[i][1] == 'man'])
only_man = [group_people[i] for i in range(len(group_people)) if group_people[i][1] == 'man']
tall_man = [only_man[i] for i in range(len(only_man)) if only_man[i][2] == max(i[2] for i in only_man)]

#-------- check if there are two people of the same height in the group ----------------------------------
count = 0
flag = False
for i in range(len(group_people)):
    for j in range(len(group_people)):
        if group_people[i][2] == group_people[j][2]:
            count += 1
    if count > 1:
        flag = True
    count = 0

print(total_woman / count_woman, *tall_man, flag, sep='\n')