"""
Создайте словарь, где ключами являются числа, а значениями – строки.
Примените к нему метод items(), полученный объект dict_items передайте в написанную вами функцию,
которая создает и возвращает новый словарь, "обратный" исходному, т. е. ключами являются строки, а значениями – числа.

"""

# create dictionary
dictionary = {'a': 1, 'b': 2, 'c': 3,
              'd': 4, 'e': 5, 'f': 6,
              'g': 7, 'h': 8, 'i': 9}

# This is function which will reverse dictionary
def function_reverse():
    reverse_dictionary = {}
    for key, value in dictionary.items():
        reverse_dictionary.setdefault(value, key)
    return reverse_dictionary


# output reverse dictionary
print(function_reverse())









