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

        for i in range(8):
            self.data.put_number(f"number{i}", i)
        for i in range(8):
            self.data.put_boolean(f"bool{i}", (i % 2) == 0)
        for i in range(8):
            self.data.put_text(f"text{i}", f"t{i}t")

    def run(self) -> None:
        super().run()

    def stop(self) -> None:
        super().stop()
