"""
Вагою числової множини називається сума модулів всіх його
елементів. Вага порожньої множини вважається рівною нулеві. Скласти
програму для обчислення ваги числової множини.

"""
s = {21, 22, -2, 31, -10, -20, 1}

for i in s:
    if i < 0:
        s.remove(i)
        s.add(abs(i))

print(sum(s))