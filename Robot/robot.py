# from robotmap import RobotMap
from basemap import BaseMap
from pibot.base.baserobot import BaseRobot
from pibot.base.commands.command import Command

DRIVE_SPEED = 1.0


class Robot(BaseRobot):
    def __init__(self) -> None:
        super().__init__()
        robot_map = BaseMap()
        self.data.put_text("Hello", "World")
        self.data.put_boolean("bol", True)
        self.data.put_number("num", 3.1415926)

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
