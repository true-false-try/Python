"""
У двох списках міститься таблиця футбольного турніру. У
першому спску записано назви команд. У другому списку – результати
матчів.
(команда1, команда2, m1, m2)
де, команда1, команда2 –перша та друга команда;
m1, m2 – кількість м’ячів, забитих відповідно першою та другою командою.
Показати команду, яка є лідером, якщо за перемогу нараховується 3 очки, за
нічию – 1, за поразку – 0.
З двох команд, які мають однакову кількість очок, першою вважається та, яка
 1) має кращу різницю забитих та пропущених м’ячів;
 2) при однаковій різниці має більше забитих м’ячів;
Показати поточну таблицю турніру у вигляді:
місце, команда, ігор, виграшів, нічиїх, поразок, м’ячів забито, м’ячів
пропущено, очок
Вказівка. Створити словник таблиці турніру з ключем Команда та кортежем.

"""
import random as rn

lst_teams_names = ['Барселона', 'Арсенал', 'Манчестер Юнайтед',
                   'Реал Мадрид', 'Спартак', 'Челси',
                   'Ливерпуль', 'Рубин', 'Динамо']

# create tuple score
lst_score = tuple([i, rn.choice(lst_teams_names),
                   rn.randint(0, 5), rn.randint(0, 5)] for i in lst_teams_names)

# this block of code changes the team name in the right column so that the team cannot play against itself
for i in range(len(lst_score)):
    if lst_score[i][0] == lst_score[i][1]:
        lst_score[i][1] = rn.choice(lst_teams_names)


# this function displays a dictionary with all the values requested in the problem statement
def winner_team():
    team_dictionary = {}
    lst_mark = []
    mark, games, win, none, lose, goals, miss = 0, 0, 0, 0, 0, 0, 0

    # this block generates streaming values of each command
    for i in range(len(lst_score)):
        for j in range(len(lst_score)):
            if lst_score[i][0] == lst_score[j][0]:
                if lst_score[j][2] > lst_score[j][3]:
                    mark += 3
                    games += 1
                    win += 1
                    goals += lst_score[j][2]
                elif lst_score[j][2] == lst_score[j][3]:
                    mark += 1
                    games += 1
                    none += 1
                    miss += lst_score[j][3]
                else:
                    games += 1
                    lose += 1
                    miss += lst_score[j][3]

            if lst_score[i][0] == lst_score[j][1]:
                if lst_score[j][2] < lst_score[j][3]:
                    mark += 3
                    games += 1
                    win += 1
                    goals += lst_score[j][3]
                elif lst_score[j][2] == lst_score[j][3]:
                    mark += 1
                    games += 1
                    none += 1
                    miss += lst_score[j][2]
                else:
                    games += 1
                    lose += 1
                    miss += lst_score[j][3]

        # creating list with mark
        lst_mark.append(mark)

        # creating dictionary, where key is a name team and values are tuple
        team_dictionary.setdefault(lst_score[i][0], (lst_score[i][0], games, win, none, lose, goals, miss, mark))

        mark, games, win, none, lose, goals, miss = 0, 0, 0, 0, 0, 0, 0

    count_place = 0
    dictionary_place = {}

    # sorting on marks and if mark first team == mark second team count
    # by the difference between scored and missed goals
    for key, value in sorted(team_dictionary.items(), key=lambda wins: (wins[1][7], wins[1][5] - wins[1][6]),
                             reverse=True):
        count_place += 1

        dictionary_place.setdefault(value[0], ('место: ' + str(count_place),
                                               'игра: ' + str(value[1]),
                                               'побед: ' + str(value[2]),
                                               'ничья: ' + str(value[3]),
                                               'поражение: ' + str(value[4]),
                                               'забито: ' + str(value[5]),
                                               'пропущено: ' + str(value[6]),
                                               'очки: ' + str(value[7])))
        print(dictionary_place, sep='\n')
        dictionary_place.clear()


# output
winner_team()
