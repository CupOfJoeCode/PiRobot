import math


class Vector:

    def __init__(self, x=0, y=0, z=0, w=0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    @classmethod
    # Only uses XY Components
    def from_angle(self, angle):
        return Vector(math.sin(angle), math.cos(angle))

    # Only uses XY Components
    def to_angle(self):
        norm = self.normalize()
        return math.atan2(norm.x, norm.y)

    # Only uses XY Components
    def rotate(self, angle):
        length = self.length
        return Vector.from_angle(self.to_angle() + angle)*length

    def length(self):
        return math.sqrt((self.x**2)+(self.y**2)+(self.z**2)+(self.w**2))

    def normalize(self):
        return self * (1 / self.length())

    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z + self.w*other.w

    def to_color(self):
        return tuple(map(lambda x: min(255, max(0, int(x*255))), [self.x, self.y, self.z, self.w]))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)
