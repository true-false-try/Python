class Point2:
    """Клас реалізує точку площини"""
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        """Повернути координату х"""
        return self._x

    def get_y(self):
        """Повернути координату y"""
        return self._y

    def __str__(self):
        """Повернути рядок представлення точки"""
        return "({}, {})".format(self._x, self._y)


class Segment:

    def __init__(self, a, b):
        self._a = a
        self._b = b

    def get_a(self):
        return self._a

    def get_b(self):
        return self._b

    def __str__(self):
        """Return line where point _a and _b"""
        return "({}, {})".format(self._a, self._b)

    def len(self):
        return (self._a.get_x() - self._b.get_x()) + \
               (self._a.get_y() - self._b.get_y())


class Rectangle:

    def __init__(self, a, b, c, d):
        self._a = a
        self._b = b
        self._c = c
        self._d = d

    def get_a(self):
        return self._a

    def get_b(self):
        return self._b

    def get_c(self):
        return self._c

    def get_d(self):
        return self._d

    def _get_sides(self):
        s1 = Segment(self._a, self._b).len()
        s2 = Segment(self._a, self._b).len()
        s3 = Segment(self._a, self._b).len()
        s4 = Segment(self._a, self._b).len()
        return s1, s2, s3, s4

    def perimeter(self):
        s1, s2, s3, s4 = self._get_sides()
        return s1, s2, s3, s4

    def square(self):
        p = self.perimeter()
        s1, s2, s3, s4 = self._get_sides()
        return s1 * s2

    def __str__(self):
        return "({}, {}, {}, {})".format(self._a, self._b, self._c, self._d)
