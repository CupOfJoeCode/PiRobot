from pibot.rpihbridge import RpiHBridge
from pibot.base.baserobot import BaseRobot
from pibot.base.command import Command

MOTOR_FREQ = 5000
DRIVE_SPEED = 1.0

class Robot(BaseRobot):

    def drive(self, left_speed, right_speed):
        def set_motors():
            self.left_motor.set(left_speed)
            self.right_motor.set(right_speed)
        def reset_motors():
            self.leftMotor.stop()
            self.rightMotor.stop()
        return Command('Drive').initialize(set_motors).end(reset_motors)
    
    def __init__(self):
        super().__init__()
        self.left_motor = RpiHBridge(26, 19, pwm_freq=MOTOR_FREQ)
        self.right_motor = RpiHBridge(13, 12, pwm_freq=MOTOR_FREQ)

        self.bind('up', self.drive(1.0,1.0))
        self.bind('down', self.drive(-1.0,-1.0))
        self.bind('left', self.drive(-1.0,1.0))
        self.bind('right', self.drive(1.0,-1.0))

    def run(self):
        super().run()

    def stop(self):
        super().stop()
        self.leftMotor.stop()
        self.rightMotor.stop()