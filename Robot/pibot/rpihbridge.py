from pibot.base.motor import Motor
from pibot.rpipwm import RpiPWMOutput
from pibot.rpioutput import RpiOutput


class RpiHBridge(Motor):

    def __init__(self, speed_pin, dir_pin, pwm_freq=100):
        super().__init__()
        self.pwm = RpiPWMOutput(speed_pin, pwm_freq)
        self.direction = RpiOutput(dir_pin)
        self.speed = 0
        self.pwm.set(0)
        self.direction.set(False)

    def set(self, speed):
        self.pwm.set(abs(speed))
        self.direction.set(speed < 0)
        self.speed = speed

    def get(self):
        return super().get()
