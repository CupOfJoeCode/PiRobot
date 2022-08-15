from base.digitalout import DigitalOutput


class RpiOutput(DigitalOutput):
    def __init__(self):
        super().__init__()

    def write(self, state):
        return super().write(state)
