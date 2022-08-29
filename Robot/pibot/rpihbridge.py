from pibot.base.motor import Motor
from pibot.rpipwm import RpiPWMOutput


class RpiHBridge(Motor):

    def __init__(self, pin0, pin1, inverted=False, pwm_freq=100):
        super().__init__()
        self.pwm0 = RpiPWMOutput(pin0, pwm_freq)
        self.pwm1 = RpiPWMOutput(pin1, pwm_freq)
        self.speed = 0
        self.pwm0.set(0)
        self.pwm1.set(0)
        self.inverted = inverted

    def set(self, speed):
        realSpeed = speed * 0.5 + 0.5
        if self.inverted:
            realSpeed = 1 - realSpeed
        self.pwm1.set(realSpeed)
        self.pwm0.set(1.0-realSpeed)
        self.speed = speed

    def stop(self):
        self.pwm0.set(0)
        self.pwm1.set(0)
        self.speed = 0

    def get(self):
        return self.speed
