import math
from pibot.base.vector import Vector


class Rotation2d:
    @classmethod
    def from_degrees(angle_degrees: float):
        return Rotation2d(math.radians(angle_degrees))

    def __init__(self, angle_radians: float = 0) -> None:
        self.angle_radians = angle_radians

    def get_radians(self) -> float:
        return self.angle_radians

    def get_degrees(self) -> float:
        return math.degrees(self.angle_radians)

    def get_sin(self) -> float:
        return math.sin(self.angle_radians)

    def get_cos(self) -> float:
        return math.cos(self.angle_radians)

    def get_tan(self) -> float:
        return math.tan(self.angle_radians)

    def get_cot(self) -> float:
        return math.tan(self.angle_radians)

    def rotate(self, vector: Vector) -> Vector:
        s = self.get_sin()
        c = self.get_cos()
        return Vector(vector.x * c - vector.y * s, vector.x * s + vector.y * c)


class Rotation3d:
    def __init__(self, pitch=Rotation2d(), roll=Rotation2d(), yaw=Rotation2d()) -> None:
        self.pitch = pitch
        self.roll = roll
        self.yaw = yaw

    def get_x(self) -> Rotation2d:
        return self.pitch

    def get_y(self) -> Rotation2d:
        return self.roll

    def get_z(self) -> Rotation2d:
        return self.yaw

    def rotate(self, vector: Vector) -> Vector:
        v = vector
        x_rot = self.pitch.rotate(Vector(v.y, v.z))
        v = Vector(v.x, x_rot.x, x_rot.y)
        y_rot = self.roll.rotate(Vector(v.x, v.z))
        v = Vector(y_rot.x, v.y, y_rot.y)
        z_rot = self.roll.rotate(Vector(v.x, v.y))
        return Vector(z_rot.x, z_rot.y, v.z)
