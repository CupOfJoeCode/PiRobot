import math


class Vector:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0, w: float = 0) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    @classmethod
    def from_color(color: tuple[int]):
        return Vector(color[0] / 255.0, color[1] / 255.0, color[2] / 255.0)

    def length(self) -> float:
        return math.sqrt((self.x**2) + (self.y**2) + (self.z**2) + (self.w**2))

    def normalize(self):
        return self * (1 / self.length())

    def dot(self, other) -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w

    def to_color(self) -> tuple[int]:
        return tuple(min(255, max(0, int(x * 255))) for x in [self.x, self.y, self.z])

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)
