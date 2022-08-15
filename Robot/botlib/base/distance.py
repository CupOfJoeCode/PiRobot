class DistanceSensor:
    def __init__(self):
        pass

    def get_raw(self):
        return 0

    def get_centimeters(self):
        return (self.get_raw() * 34300) / 2.0

    def get_meters(self):
        return self.get_centimeters() / 100.0

    def get_inches(self):
        return self.get_centimeters() / 2.54

    def get_feet(self):
        return self.get_inches() / 12.0
