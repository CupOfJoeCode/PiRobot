from pibot.rpioutput import RpiOutput
from pibot.rpiinput import RpiInput
from pibot.base.distance import DistanceSensor
import time


class RpiUltraSonic(DistanceSensor):

    def __init__(self, trig_pin, echo_pin):
        super().__init__()
        self.trigger = RpiOutput(trig_pin)
        self.echo = RpiInput(echo_pin)

    def get_seconds(self, timeout=1.0):
        start_time = time.time()
        self.trigger.pulse()
        while not self.echo.get():
            delta_time = time.time() - start_time
            if delta_time > timeout:
                break
        return delta_time
