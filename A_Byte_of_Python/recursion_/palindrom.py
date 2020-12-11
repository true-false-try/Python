def palindrom(string):
    if len(string) <= 1:
        return True
    elif string[0] != string[-1]:
        return False
    return palindrom(string[1:-1])

print(palindrom('zabcbac'))


