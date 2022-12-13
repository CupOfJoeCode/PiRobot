from basemap import BaseMap
from pibot.rpihbridge import RpiHBridge
MOTOR_FREQ = 5000


class RobotMap(BaseMap):
    def __init__(self):
        pass

    def get_left_motor(self):
        return RpiHBridge(26, 19, pwm_freq=MOTOR_FREQ)

    def get_right_motor(self):
        return RpiHBridge(13, 12, pwm_freq=MOTOR_FREQ)
