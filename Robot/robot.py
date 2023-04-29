# from robotmap import RobotMap
from basemap import BaseMap
from pibot.base.baserobot import BaseRobot
from pibot.base.pose import Pose2d, Pose3d
from pibot.base.units import Distance, Angle
from pibot.base.rotation import Rotation2d

DRIVE_SPEED = 1.0


class Robot(BaseRobot):
    def __init__(self) -> None:
        super().__init__()
        robot_map = BaseMap()

        pose_test = Pose2d(
            Distance.from_meters(1),
            Distance.from_meters(-0.5),
            Rotation2d(Angle.from_degrees(45)),
        )

        self.data.put_pose2d("pose", pose_test)

        self.left_motor = robot_map.get_left_motor()
        self.right_motor = robot_map.get_right_motor()

    def drive(self, left: float, right: float) -> None:
        self.left_motor.set(left)
        self.right_motor.set(right)

    def run(self) -> None:
        super().run()
        if self.triggered("up"):
            self.drive(1.0, 1.0)
        elif self.triggered("down"):
            self.drive(-1.0, -1.0)

        if self.triggered("left"):
            self.drive(-1.0, 1.0)

    def stop(self) -> None:
        super().stop()
        self.left_motor.stop()
        self.right_motor.stop()
