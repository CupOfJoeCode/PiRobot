from time import sleep


class DigitalOutput:
    def __init__(self):
        self.state = False

    def write(self, state):
        self.state = state

    def set(self):
        self.write(True)

    def reset(self):
        self.write(False)

    def pulse(self, time=0.01, low=False):
        self.write(True != low)
        sleep(time)
        self.write(False != low)
