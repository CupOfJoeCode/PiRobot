

from pibot.base.baserobot import BaseRobot
from pibot.base.command import Command
# from robotmap import RobotMap
from basemap import BaseMap

DRIVE_SPEED = 1.0


class Robot(BaseRobot):

    def drive(self, left_speed, right_speed):
        def set_motors():
            self.left_motor.set(left_speed)
            self.right_motor.set(right_speed)

        def reset_motors():
            self.left_motor.stop()
            self.right_motor.stop()
        return Command('Drive').initialize(set_motors).end(reset_motors)

    def __init__(self):
        super().__init__()
        robot_map = BaseMap()

        self.left_motor = robot_map.get_left_motor()
        self.right_motor = robot_map.get_right_motor()

        self.bind('up', self.drive(1.0, 1.0))
        self.bind('down', self.drive(-1.0, -1.0))
        self.bind('left', self.drive(-1.0, 1.0))
        self.bind('right', self.drive(1.0, -1.0))

    def run(self):
        super().run()

    def stop(self):
        super().stop()
        self.left_motor.stop()
        self.right_motor.stop()
