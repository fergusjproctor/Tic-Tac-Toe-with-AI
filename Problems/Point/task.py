import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        return math.sqrt(((self.x - other_point.x) ** 2) + ((self.y - other_point.y) ** 2))
