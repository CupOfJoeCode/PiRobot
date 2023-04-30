from pibot.base.pose import Pose2d
from pibot.base.rotation import Rotation2d
from pibot.base.units import Distance, Angle


class VirtualDiffDrive:
    def __init__(
        self, forward_acceleration: Distance, angle_acceleration: Angle, friction: float
    ):
        self._pose = Pose2d()
        self._angle_vel = Angle(0)
        self._forward_vel = Distance(0)
        self._friction = friction
        self._forward_max_vel = forward_acceleration
        self._angle_max_vel = angle_acceleration

    def drive(self, left_speed, right_speed):
        self._forward_vel += self._forward_max_vel * ((left_speed + right_speed) * 0.5)
        self._angle_vel += self._angle_max_vel * ((right_speed - left_speed) * 0.5)

    def update(self):
        self._pose = Pose2d(
            self._pose.get_x()
            + (self._forward_vel * self._pose.get_rotation().get_cos()),
            self._pose.get_y()
            + (self._forward_vel * self._pose.get_rotation().get_sin()),
            Rotation2d(self._pose.get_rotation().get_angle() + self._angle_vel),
        )

        self._forward_vel *= self._friction
        self._angle_vel *= self._friction
        return self._pose
