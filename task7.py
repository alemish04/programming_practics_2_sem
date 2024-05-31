class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


class Rect:
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def __str__(self):
        return f"Rect({str(self.top_left)}, {str(self.bottom_right)})"

    def sides(self):
        return abs(self.bottom_right.x - self.top_left.x), abs(self.bottom_right.y - self.top_left.y)

    def perim(self):
        a, b = self.sides()
        return 2 * (a + b)


top_left = Point(0, 10)
bottom_right = Point(10, 0)
rect = Rect(top_left, bottom_right)
print(rect.sides())
print(rect.perim())
