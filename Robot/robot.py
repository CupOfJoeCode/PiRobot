from pibot.rpihbridge import RpiHBridge
# from pibot.vision import *
MOTOR_FREQ = 5000


class Robot:
    def __init__(self):
        self.data = {
            'speed': 1.0
        }
        self.running = False

        self.leftMotor = RpiHBridge(26, 19, pwm_freq=MOTOR_FREQ)
        self.rightMotor = RpiHBridge(13, 12, pwm_freq=MOTOR_FREQ)

        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def run(self):
        if self.up:
            self.leftMotor.set(self.data['speed'])
            self.rightMotor.set(self.data['speed'])
        else:
            self.leftMotor.set(0)
            self.rightMotor.set(0)

    def stop(self):
        self.leftMotor.stop()
        self.rightMotor.stop()

    def trigger_start(self, trigger):
        if trigger == 'up':
            self.up = True
        elif trigger == 'down':
            self.down = True
        elif trigger == 'left':
            self.left = True
        elif trigger == 'right':
            self.right = True

    def trigger_end(self, trigger):
        if trigger == 'up':
            self.up = False
        elif trigger == 'down':
            self.down = False
        elif trigger == 'left':
            self.left = False
        elif trigger == 'right':
            self.right = False
