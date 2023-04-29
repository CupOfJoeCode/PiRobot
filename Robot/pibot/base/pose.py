from pibot.base.rotation import Rotation2d, Rotation3d
from pibot.base.vector import Vector
from pibot.base.units import Distance


class Pose2d:
    def __init__(
        self,
        x: Distance = Distance(0),
        y: Distance = Distance(0),
        rotation: Rotation2d = Rotation2d(),
    ) -> None:
        self._position = Vector(x.get_meters(), y.get_meters())
        self._rotation = rotation

    def get_x(self) -> Distance:
        return Distance.from_meters(self._position.x)

    def get_y_meters(self) -> Distance:
        return Distance.from_meters(self._position.y)

    def get_rotation(self) -> Rotation2d:
        return self._rotation


class Pose3d:
    def __init__(
        self,
        x: Distance = Distance(0),
        y: Distance = Distance(0),
        z: Distance = Distance(0),
        rotation: Rotation3d = Rotation3d(),
    ) -> None:
        self._position = Vector(x.get_meters(), y.get_meters(), z.get_meters())
        self._rotation = rotation

    def get_x(self) -> Distance:
        return Distance.from_meters(self._position.x)

    def get_y(self) -> Distance:
        return Distance.from_meters(self._position.y)

    def get_z(self) -> Distance:
        return Distance.from_meters(self._position.z)

    def get_rotation(self) -> Rotation3d:
        return self._rotation

    def to_pose2d(self) -> Pose2d:
        return Pose2d(self.get_x(), self.get_y(), self._rotation.get_z())
