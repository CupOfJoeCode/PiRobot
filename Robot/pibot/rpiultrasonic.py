from pibot.rpioutput import RpiOutput
from pibot.rpiinput import RpiInput
from pibot.base.distance import DistanceSensor
from pibot.base.timer import Timer


class RpiUltraSonic(DistanceSensor):

    def __init__(self, trig_pin, echo_pin):
        super().__init__()
        self.trigger = RpiOutput(trig_pin)
        self.echo = RpiInput(echo_pin)
        self.timer = Timer()

    def get_seconds(self, timeout=1.0):
        self.timer.start()
        self.trigger.pulse()
        while (not self.echo.get()) and (self.timer.get_seconds() < timeout):
            pass
        return self.timer.get_seconds()
