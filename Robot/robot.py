from pibot.rpihbridge import RpiHBridge
from pibot.rpioutput import RpiOutput

MOTOR_FREQ = 5000


class Robot:
    def __init__(self):
        self.data = {
            'Speed': 0.0,
            'On': False
        }
        self.running = False
        self.motor = RpiHBridge(12, 19, pwm_freq=MOTOR_FREQ)

    def run(self):
        self.data['Speed'] = min(1, max(-1, self.data['Speed']))
        self.motor.set(self.data['Speed'])
        # self.output.write(self.data['On'])

    def stop(self):
        self.motor.stop()
        self.data['Speed'] = 0.0

    def trigger_start(self, trigger):
        if trigger == 'up':
            self.data['Speed'] += 0.05
        elif trigger == 'down':
            self.data['Speed'] -= 0.05

    def trigger_end(self, trigger):
        pass
