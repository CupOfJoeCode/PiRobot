class DistanceSensor:
    def __init__(self) -> None:
        pass

    def get_seconds(self) -> float:
        return 0

    def get_centimeters(self) -> float:
        return (self.get_seconds() * 34300) / 2.0

    def get_meters(self) -> float:
        return self.get_centimeters() / 100.0

    def get_inches(self) -> float:
        return self.get_centimeters() / 2.54

    def get_feet(self) -> float:
        return self.get_inches() / 12.0
