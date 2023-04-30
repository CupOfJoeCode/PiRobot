from pibot.base.pose import Pose2d
from pibot.base.rotation import Rotation2d
from pibot.base.units import Distance, Angle
import math


class VirtualDiffDrive:
    def __init__(self, forward_acc: Distance, angle_acc: Angle, friction: float):
        self.pose = Pose2d()
        self.angle_vel = Angle(0)
        self.forward_vel = Distance(0)
        self.friction = friction
        self.forward_max_vel = forward_acc
        self.angle_max_vel = angle_acc

    def drive(self, left_speed, right_speed):
        vf = self.forward_max_vel * ((left_speed + right_speed) * 0.5)
        vr = self.angle_max_vel * ((right_speed - left_speed) * 0.5)

        self.forward_vel += vf
        self.angle_vel += vr

    def get_pose(self):
        self.pose = Pose2d(
            self.pose.get_x() + (self.forward_vel * self.pose.get_rotation().get_cos()),
            self.pose.get_y() + (self.forward_vel * self.pose.get_rotation().get_sin()),
            Rotation2d(self.pose.get_rotation().get_angle() + self.angle_vel),
        )

        self.forward_vel *= self.friction
        self.angle_vel *= self.friction
        return self.pose
