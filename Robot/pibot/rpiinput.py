from base.digitalin import DigitalInput


class RpiInput(DigitalInput):
    def __init__(self):
        super().__init__()

    def get(self):
        return super().get()
