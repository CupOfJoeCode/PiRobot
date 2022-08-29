from pibot.rpihbridge import RpiHBridge

MOTOR_FREQ = 2000


class Robot:
    def __init__(self):
        self.data = {
            'Speed': 0.6,
            'Left': True,
            'Right': True
        }
        self.running = False
        self.leftMotor = RpiHBridge(26, 19, pwm_freq=MOTOR_FREQ)
        self.rightMotor = RpiHBridge(13, 12, pwm_freq=MOTOR_FREQ)

        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def run(self):
        leftSpeed = 1.0 if self.data['Left'] else 0.0
        rightSpeed = 1.0 if self.data['Right'] else 0.0
        if self.up:
            self.leftMotor.set(self.data['Speed'] * leftSpeed)
            self.rightMotor.set(self.data['Speed'] * rightSpeed)
        elif self.down:
            self.leftMotor.set(-self.data['Speed'] * leftSpeed)
            self.rightMotor.set(-self.data['Speed'] * rightSpeed)
        elif self.left:
            self.leftMotor.set(self.data['Speed'] * leftSpeed)
            self.rightMotor.set(-self.data['Speed'] * rightSpeed)
        elif self.right:
            self.leftMotor.set(-self.data['Speed'] * leftSpeed)
            self.rightMotor.set(self.data['Speed'] * rightSpeed)
        else:
            self.leftMotor.stop()
            self.rightMotor.stop()

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
