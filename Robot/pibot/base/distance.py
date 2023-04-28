from pibot.base.units import Distance, Time


class DistanceSensor:
    def __init__(self) -> None:
        pass

    def get_time(self) -> Time:
        return Time(0)

    def get_distance(self) -> Distance:
        return Distance.from_centimeters((self.get_time().get_seconds() * 34300) / 2.0)
