from pibot.base.motor import Motor


class RpiHBridge(Motor):

    def __init__(self):
        super().__init__()

    def set(self, speed):
        return super().set(speed)

    def get(self):
        return super().get()
