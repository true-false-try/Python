import shelve

file = shelve.open('dictionary_books')

"""with file as books:
    books["451° по Фаренгейту"] = "Рей Брэдбери", 1965
    books["1984"] = "Джордж Оруэлл", 1984
    books["Вино из одуванчиков"] = "Рей Брэдбери", 1965
    books["Мастер и Маргарита"] = "Михаил Булгаков", 1936
    books["Три товарища"] = "Эрих Мария Ремарк", 1943
    books["Над пропастью во ржи"] = "Джером Д. Сэлинджер", 1949
    books["Цветы для Элджернона"] = "Даниел Киз", 1999
    books["Сто лет одиночества"] = "Габриэль Гарсиа Маркес", 1963
    books["Атлант расправил плечи"] = "Айн Рэнд", 1985
    books["Портрет Дориана Грея"] = "Оскар Уайльд", 1941"""


def list_writers():
    print('List writer:')
    lst_writers = []
    for k, v in file.items():
        lst_writers.append(file[k][0])
    lst_writers = sorted(list(set(lst_writers)))
    return lst_writers


print(*list_writers(), sep="\n")


# a)
def sort_writer_1960(string):
    count = 0
    for k, v in file.items():
        if string == file[k][0] and file[k][1] > 1960:
            print(k, '\t', *v, sep='\t')
            count += 1
    if count <= 0:
        print("Not found")


sort_writer_1960(str(input('Write name writer from list above this massage:')))


# b)
def book_name(string):
    count = 0
    for k, v in file.items():
        if string == k:
            print(k, '\t', *v, sep='\t')
            count += 1
    if count <= 0:
        print("Not found")


book_name(str(input('Enter book name:')))





