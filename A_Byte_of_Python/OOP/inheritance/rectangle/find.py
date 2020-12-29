from A_Byte_of_Python.OOP.inheritance.rectangle.coordinates import Point2, Segment, Rectangle


def input_point(name):
    print('Please enter 4 point {}'.format(name))
    str_xy = input('(x, y) = ')
    lst_xy = str_xy.strip('()').split(',')
    x, y = map(float, lst_xy)
    return Point2(x, y)


def _is_valid_rectangle(a, b, c, d):
    s1 = Segment(a, b).len()
    s2 = Segment(b, c).len()
    s3 = Segment(c, d).len()
    s4 = Segment(d, a).len()
    return s1 + s2 > s3 and s2 + s3 > s1


def input_rectangle(m):
    while True:
        print('Please enter point for rectangle {}'.format(m))
        a = input_point('a')
        b = input_point('b')
        c = input_point('c')
        d = input_point('d')
        if _is_valid_rectangle(a, b, c, d):
            break
        print('Rectangle is valid {} {} {} {}'.format(a, b, c, d))
        return Rectangle(a, b, c, d)




if __name__ == '__main__':
    while True:
        n = int(input('Please, enter values for count rectangle do you want (value > 0): '))
        if n > 0:
            break

    rectangles = []
    for i in range(n):
        rectangles.append(input_rectangle(i+1))

    max_p, max_s = 0, 0
    k_p, k_s = 0, 0
    for i, t in enumerate(rectangles):
        if t.perimeter() > max_p:
            max_p = t.perimeter()
            k_p = i

        if t.square() > max_s:
            max_s = t.square()
            k_s = i

    print(rectangles[k_p])
    print(rectangles[k_s])