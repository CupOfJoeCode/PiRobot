import math
from pibot.base.units import Angle
from pibot.base.vector import Vector


class Rotation2d:
    def __init__(self, angle: Angle = Angle(0)) -> None:
        self._angle = angle

    def get_angle(self) -> Angle:
        return self._angle

    def get_sin(self) -> float:
        return math.sin(self._angle.get_radians())

    def get_cos(self) -> float:
        return math.cos(self._angle.get_radians())

    def get_tan(self) -> float:
        return math.tan(self._angle.get_radians())

    def get_cot(self) -> float:
        return math.tan(self._angle.get_radians())

    def rotate(self, vector: Vector) -> Vector:
        s = self.get_sin()
        c = self.get_cos()
        return Vector(vector.x * c - vector.y * s, vector.x * s + vector.y * c)


class Rotation3d:
    def __init__(
        self,
        pitch: Angle = Angle(0),
        roll: Angle = Angle(0),
        yaw: Angle = Angle(0),
    ) -> None:
        self._pitch = Rotation2d(pitch)
        self._roll = Rotation2d(roll)
        self._yaw = Rotation2d(yaw)

    def get_x(self) -> Angle:
        return self._pitch.get_angle()

    def get_y(self) -> Angle:
        return self._roll.get_angle()

    def get_z(self) -> Angle:
        return self._yaw.get_angle()

    def get_pitch(self) -> Angle:
        return self.get_x()

    def get_roll(self) -> Angle:
        return self.get_y()

    def get_yaw(self) -> Angle:
        return self.get_z()

    def rotate(self, vector: Vector) -> Vector:
        v = vector
        x_rot = self._pitch.rotate(Vector(v.y, v.z))
        v = Vector(v.x, x_rot.x, x_rot.y)
        y_rot = self._roll.rotate(Vector(v.x, v.z))
        v = Vector(y_rot.x, v.y, y_rot.y)
        z_rot = self._roll.rotate(Vector(v.x, v.y))
        return Vector(z_rot.x, z_rot.y, v.z)
