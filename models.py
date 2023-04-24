import math
def vector_product(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def len(self):
        return math.sqrt((self.point2.x - self.point1.x) ** 2 + (self.point2.y - self.point1.y) ** 2)

    def __lt__(self, other):
        return self.len() < other.len()

    def intersection_point(self, an_line):
        x1, y1 = an_line.point1.x, an_line.point1.y
        v1 = (x1 - self.point1.x, y1 - self.point1.y)
        v2 = (x1 - self.point2.x, y1 - self.point2.y)
        print(vector_product(v1, v2))
        x2, y2 = an_line.point2.x, an_line.point2.y
        v1 = (x2 - self.point1.x, y2 - self.point1.y)
        v2 = (x2 - self.point2.x, y2 - self.point2.y)
        print(vector_product(v1, v2))


class circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        self.lines = None

    def line_intersection(self, line):
        x1, y1 = line.point1.x, line.point1.y
        x2, y2 = line.point2.x, line.point2.y

        k = (y2 - y1) / (x2 - x1)
        d = (y1 * x2 - y2 * x1) / (x2 - x1)


        a = 1 + k * k
        b = - 2 * self.center.x + 2 * k * (d - self.center.y)
        c = ((d - self.center.y) ** 2) + (self.center.x ** 2) - (self.radius ** 2)
        D = b * b - 4 * a * c

        min_x = min(x1, x2)
        max_x = max(x1, x2)

        if (D >= 0):
            one = (-b - math.sqrt(D)) / (2 * a)
            two = (-b + math.sqrt(D)) / (2 * a)
            if (min_x < one and one < max_x or min_x < two and two < max_x):
                return True
            else: return  False
        else: return False

    def __lt__(self, other):
        return self.radius < other.radius

    def set_lines(self, lines):
        self.lines = lines.copy()