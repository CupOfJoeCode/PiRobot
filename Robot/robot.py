# from robotmap import RobotMap
from basemap import BaseMap
from pibot.base.baserobot import BaseRobot
from pibot.base.pose import Pose2d
from pibot.base.units import Distance, Angle
from pibot.base.rotation import Rotation2d


class Robot(BaseRobot):
    def __init__(self) -> None:
        super().__init__()
        robot_map = BaseMap()
        self.data.put_pose2d(
            "current", Pose2d(rotation=Rotation2d(Angle.from_degrees(45)))
        )
        self.data.put_pose2d("target", Pose2d(Distance(4), Distance(3)))

    def run(self) -> None:
        super().run()
        while True:
            pass

    def stop(self) -> None:
        super().stop()
