import math


class Distance:
    @classmethod
    def from_meters(self, meters: float):
        return Distance(meters)

    @classmethod
    def from_centimeters(self, centimeters: float):
        return Distance(centimeters / Distance(1).get_centimeters())

    @classmethod
    def from_millimeters(self, millimeters: float):
        return Distance(millimeters / Distance(1).get_millimeters())

    @classmethod
    def from_kilometers(self, kilometers: float):
        return Distance(kilometers / Distance(1).get_kilometers())

    @classmethod
    def from_inches(self, inches: float):
        return Distance(inches / Distance(1).get_inches())

    @classmethod
    def from_feet(self, feet: float):
        return Distance(feet / Distance(1).get_feet())

    @classmethod
    def from_yards(self, yards: float):
        return Distance(yards / Distance(1).get_yards())

    @classmethod
    def from_miles(self, miles: float):
        return Distance(miles / Distance(1).get_miles())

    @classmethod
    def from_thou(self, thou: float):
        return Distance(thou / Distance(1).get_thou())

    def __init__(self, meters: float):
        self._meters = meters

    def get_meters(self) -> float:
        return self._meters

    def get_centimeters(self) -> float:
        return self._meters * 100.0

    def get_millimeters(self) -> float:
        return self._meters * 1000.0

    def get_kilometers(self) -> float:
        return self._meters / 1000.0

    def get_inches(self) -> float:
        return self.get_centimeters() / 2.54

    def get_feet(self) -> float:
        return self.get_inches() / 12.0

    def get_yards(self) -> float:
        return self.get_feet() / 3.0

    def get_miles(self) -> float:
        return self.get_feet() / 5280.0

    def get_thou(self) -> float:
        return self.get_inches() * 1000.0

    def __add__(self, other):
        return Distance(self._meters + other.get_meters())

    def __sub__(self, other):
        return Distance(self._meters - other.get_meters())

    def __mul__(self, other: float):
        return Distance(self._meters * other)

    def __truediv__(self, other: float):
        return Distance(self._meters / other)


class Angle:
    @classmethod
    def from_radians(self, radians: float):
        return Angle(radians)

    @classmethod
    def from_degrees(self, degrees: float):
        return Angle(degrees / Angle(1).get_degrees())

    @classmethod
    def from_rotations(self, rotations: float):
        return Angle(rotations / Angle(1).get_rotations())

    def __init__(self, radians: float):
        self._radians = radians

    def get_radians(self) -> float:
        return self._radians

    def get_degrees(self) -> float:
        return math.degrees(self._radians)

    def get_rotations(self) -> float:
        return self.get_degrees() / 360.0

    def __add__(self, other):
        return Angle(self._radians + other.get_radians())

    def __sub__(self, other):
        return Angle(self._radians - other.get_radians())

    def __mul__(self, other: float):
        return Angle(self._radians * other)

    def __truediv__(self, other: float):
        return Angle(self._radians / other)


class Time:
    @classmethod
    def from_seconds(self, seconds: float):
        return Time(seconds)

    @classmethod
    def from_minutes(self, minutes: float):
        return Time(minutes / Time(1).get_minutes())

    @classmethod
    def from_hours(self, hours: float):
        return Time(hours / Time(1).get_hours())

    @classmethod
    def from_days(self, days: float):
        return Time(days / Time(1).get_days())

    @classmethod
    def from_weeks(self, weeks: float):
        return Time(weeks / Time(1).get_weeks())

    @classmethod
    def from_years(self, years: float):
        return Time(years / Time(1).get_years())

    @classmethod
    def from_milliseconds(self, milliseconds: float):
        return Time(milliseconds / Time(1).get_milliseconds())

    @classmethod
    def from_microseconds(self, microseconds: float):
        return Time(microseconds / Time(1).get_microseconds())

    def __init__(self, seconds: float):
        self._seconds = seconds

    def get_seconds(self) -> float:
        return self._seconds

    def get_minutes(self) -> float:
        return self._seconds / 60.0

    def get_hours(self) -> float:
        return self.get_minutes() / 60.0

    def get_days(self) -> float:
        return self.get_hours() / 24.0

    def get_weeks(self) -> float:
        return self.get_days() / 7.0

    def get_years(self) -> float:
        return self.get_days() / 365.0

    def get_milliseconds(self) -> float:
        return self._seconds * 1000

    def get_microseconds(self) -> float:
        return self._seconds * 1000000

    def __add__(self, other):
        return Time(self._seconds + other.get_seconds())

    def __sub__(self, other):
        return Time(self._seconds - other.get_seconds())

    def __mul__(self, other: float):
        return Time(self._seconds * other)

    def __truediv__(self, other: float):
        return Time(self._seconds / other)


class Temperature:
    @classmethod
    def from_kelvin(self, kelvin: float):
        return Temperature(kelvin)

    @classmethod
    def from_celcius(self, celcius: float):
        return Temperature(celcius + 273.15)

    @classmethod
    def from_fahrenheit(self, fahrenheit: float):
        return Temperature.from_celcius((fahrenheit - 32) / 1.8)

    def __init__(self, kelvin: float):
        self._kelvin = kelvin

    def get_kelvin(self) -> float:
        return self._kelvin

    def get_celcius(self) -> float:
        return self._kelvin - 273.15

    def get_fahrenheit(self) -> float:
        return (self.get_celcius() * 1.8) + 32.0


class Mass:
    # gram, kilogram, milligram, metric_ton, pound, ounce, ton

    @classmethod
    def from_grams(self, grams: float):
        return Mass(grams)

    @classmethod
    def from_kilograms(self, kilograms: float):
        return Mass(kilograms / Mass(1).get_kilograms())

    @classmethod
    def from_milligrams(self, milligrams: float):
        return Mass(milligrams / Mass(1).get_milligram())

    @classmethod
    def from_metric_tons(self, metric_tons: float):
        return Mass(metric_tons / Mass(1).get_metric_tons())

    @classmethod
    def from_pounds(self, pounds: float):
        return Mass(pounds / Mass(1).get_pounds())

    @classmethod
    def from_ounces(self, ounces: float):
        return Mass(ounces / Mass(1).get_ounces())

    @classmethod
    def from_tons(self, tons: float):
        return Mass(tons / Mass(1).get_tons())

    def __init__(self, grams: float):
        self._grams = grams

    def get_grams(self) -> float:
        return self._grams

    def get_kilograms(self) -> float:
        return self._grams / 1000.0

    def get_milligrams(self) -> float:
        return self._grams * 1000.0

    def get_metric_tons(self) -> float:
        return self.get_kilograms() / 1000.0

    def get_pounds(self) -> float:
        return self.get_kilograms() * 2.2046

    def get_ounces(self) -> float:
        return self.get_pounds() * 16.0

    def get_tons(self) -> float:
        return self.get_pounds() / 2000.0

    def __add__(self, other):
        return Mass(self._grams + other.get_grams())

    def __sub__(self, other):
        return Mass(self._grams - other.get_grams())

    def __mul__(self, other: float):
        return Mass(self._grams * other)

    def __truediv__(self, other: float):
        return Mass(self._grams / other)
