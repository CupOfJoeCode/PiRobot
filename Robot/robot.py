# from robotmap import RobotMap
from basemap import BaseMap
from pibot.base.baserobot import BaseRobot
from pibot.base.pose import Pose2d
from pibot.base.units import Distance, Angle
from pibot.base.rotation import Rotation2d
from pibot.base.pid import PID
from pibot.virtual import VirtualDiffDrive


class Robot(BaseRobot):
    def __init__(self) -> None:
        super().__init__()
        robot_map = BaseMap()

        self.drive = VirtualDiffDrive(
            Distance.from_inches(1), Angle.from_degrees(1), 0.9
        )

    def run(self) -> None:
        super().run()
        if self.triggered("up"):
            self.drive.drive(1.0, 1.0)
        elif self.triggered("down"):
            self.drive.drive(-1.0, -1.0)
        elif self.triggered("left"):
            self.drive.drive(-1.0, 1.0)
        elif self.triggered("right"):
            self.drive.drive(1.0, -1.0)
        else:
            self.drive.drive(0.0, 0.0)

        self.data.put_pose2d("pose", self.drive.update())

    def stop(self) -> None:
        super().stop()
        self.drive.drive(0.0, 0.0)
