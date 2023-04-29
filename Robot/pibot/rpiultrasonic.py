from pibot.rpioutput import RpiOutput
from pibot.rpiinput import RpiInput
from pibot.base.distance import DistanceSensor
from pibot.base.timer import Timer
from pibot.base.units import Time, Distance


class RpiUltraSonic(DistanceSensor):
    def __init__(self, trig_pin: int, echo_pin: int) -> None:
        super().__init__()
        self.trigger = RpiOutput(trig_pin)
        self.echo = RpiInput(echo_pin)
        self.timer = Timer()

    def get_distance(self) -> Distance:
        self.timer.start()
        self.trigger.pulse()
        while (not self.echo.get()) and (self.timer.get_time().get_seconds() < 0.1):
            pass

        return Distance.from_centimeters(
            (self.timer.get_time().get_seconds() * 34300) / 2.0
        )
