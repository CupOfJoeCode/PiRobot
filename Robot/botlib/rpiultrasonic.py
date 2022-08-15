from base.distance import DistanceSensor


class RpiUltraSonic(DistanceSensor):

    def __init__(self):
        super().__init__()

    def get_raw(self):
        return super().get_raw()
