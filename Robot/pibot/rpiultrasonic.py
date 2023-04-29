from pibot.rpioutput import RpiOutput
from pibot.rpiinput import RpiInput
from pibot.base.distance import DistanceSensor
from pibot.base.timer import Timer
from pibot.base.units import Time, Distance


class RpiUltraSonic(DistanceSensor):
    """
    An ultrasonic distance sensor connected to the Raspberry Pi

    Methods
    -------
    get_distance()
        Get the distance to an object
    """

    def __init__(self, trig_pin: int, echo_pin: int) -> None:
        """Create a Raspberry Pi ultrasonic distance sensor

        Parameters
        ----------
        trig_pin : int
            The trigger output pin of the sensor using the BCM pin number
        echo_pin : int
            The echo input pin of the sensor using the BCM pin number

        Returns
        -------
        None
        """
        super().__init__()
        self._trigger = RpiOutput(trig_pin)
        self._echo = RpiInput(echo_pin)
        self._timer = Timer()

    def get_distance(self) -> Distance:
        """Get the distance to an object

        Returns
        -------
        distance : Distance
            The distance reading from the sensor
        """
        self._timer.start()
        self._trigger.pulse()
        while (not self._echo.get()) and (self._timer.get_time().get_seconds() < 0.1):
            pass

        return Distance.from_centimeters(
            (self._timer.get_time().get_seconds() * 34300) / 2.0
        )
