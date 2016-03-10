import collections


class Vector2(collections.namedtuple('vector2', 'x y')):
    __slots__ = ()

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
