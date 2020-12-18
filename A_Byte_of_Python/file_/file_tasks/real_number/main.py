file = open('file_numbers.txt', 'r')

x = [i.rstrip() for i in file]
string = ' '.join(x)
lst = string.split()
convert = [int(i) for i in lst]


# a)
def total():
    global lst
    return sum([int(i) for i in lst])


# b)
def minus():
    global convert
    return sum([1 for i in convert if i < 0])


# c)
def last_numb():
    global convert
    return convert[len(convert) - 1]


# d)
def max_numb():
    global convert
    return max(convert)


# e)
def min_couple_numb():
    global convert
    return min([i for i in convert if i > 9])


# f)
def sum_min_max_numb():
    global convert
    return min([i for i in convert]) + max(i for i in convert if i)


# j)
def first_last():
    global convert
    return convert[0] - convert[len(convert) - 1]


# h)
def middle_aref():
    global convert
    return sum([1 for i in convert if i < round(total() / (len(convert) + 1))])


print('sum file:',
          total(), sep='\n')
print('count minus:',
          minus(), sep='\n')
print('last number:',
          last_numb(), sep='\n')
print('max number:',
          max_numb(), sep='\n')
print('min couple number:',
          min_couple_numb(), sep='\n')
print('min - max:',
          sum_min_max_numb(), sep='\n')
print('degree first numb and last numb:',
          first_last(), sep='\n')
print('the number of components of a file that are less than the arithmetic mean of all its components:',
          middle_aref(), sep='\n')

file.close()
