class DigitalOutput:
    def __init__(self):
        self.state = False

    def write(self, state):
        self.state = state

    def set(self):
        self.write(True)

    def reset(self):
        self.write(False)
