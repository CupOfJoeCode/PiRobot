# from robotmap import RobotMap
from basemap import BaseMap
from pibot.base.baserobot import BaseRobot


class Robot(BaseRobot):
    def __init__(self) -> None:
        super().__init__()
        robot_map = BaseMap()

    def run(self) -> None:
        super().run()

    def stop(self) -> None:
        super().stop()
