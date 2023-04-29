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

    def __mul__(self, other: float):
        return Vector(self.x * other, self.y * other, self.z * other)


class Rotation2d:
    def __init__(self, angle: float = 0) -> None:
        self._angle = angle

    def get_angle(self) -> float:
        return self._angle

    def get_sin(self) -> float:
        return math.sin(self._angle)

    def get_cos(self) -> float:
        return math.cos(self._angle)

    def get_tan(self) -> float:
        return math.tan(self._angle)

    def get_cot(self) -> float:
        return math.tan(self._angle)

    def rotate(self, vector: Vector) -> Vector:
        s = self.get_sin()
        c = self.get_cos()
        return Vector(vector.x * c - vector.y * s, vector.x * s + vector.y * c)


class Rotation3d:
    def __init__(
        self,
        pitch: float = 0,
        roll: float = 0,
        yaw: float = 0,
    ) -> None:
        self._pitch = Rotation2d(pitch)
        self._roll = Rotation2d(roll)
        self._yaw = Rotation2d(yaw)

    def get_x(self) -> float:
        return self._pitch.get_angle()

    def get_y(self) -> float:
        return self._roll.get_angle()

    def get_z(self) -> float:
        return self._yaw.get_angle()

    def get_pitch(self) -> float:
        return self.get_x()

    def get_roll(self) -> float:
        return self.get_y()

    def get_yaw(self) -> float:
        return self.get_z()

    def rotate(self, vector: Vector) -> Vector:
        v = vector
        x_rot = self._pitch.rotate(Vector(v.y, v.z))
        v = Vector(v.x, x_rot.x, x_rot.y)
        y_rot = self._roll.rotate(Vector(v.x, v.z))
        v = Vector(y_rot.x, v.y, y_rot.y)
        z_rot = self._roll.rotate(Vector(v.x, v.y))
        return Vector(z_rot.x, z_rot.y, v.z)
