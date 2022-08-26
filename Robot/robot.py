from pibot.rpihbridge import RpiHBridge

MOTOR_FREQ = 5000


class Robot:
    def __init__(self):
        self.data = {
            'SpeedLeft': 0.0,
            'SpeedRight': 0.0,
            'On': False
        }
        self.running = False
        self.leftMotor = RpiHBridge(26, 19, pwm_freq=MOTOR_FREQ)
        self.rightMotor = RpiHBridge(13, 12, pwm_freq=MOTOR_FREQ)

    def run(self):
        self.leftMotor.set(self.data['SpeedLeft'])
        self.rightMotor.set(self.data['SpeedRight'])

    def stop(self):
        self.leftMotor.stop()
        self.rightMotor.stop()

    def trigger_start(self, trigger):
        pass

    def trigger_end(self, trigger):
        pass
