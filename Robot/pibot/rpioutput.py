from pibot.base.digitalout import DigitalOutput
import RPi.GPIO as GPIO


class RpiOutput(DigitalOutput):
    """
    A digital output connected to a Raspberry Pi.
    Inherits from `DigitalOutput`

    Methods
    -------
    write(state : bool)
        Write a state to the output
    """

    def __init__(self, pin: int) -> None:
        """Create a Raspberry Pi digital output

        Parameters
        ----------
        pin : int
            The output pin of the Raspberry Pi using the BCM number

        Returns
        -------
        None
        """
        super().__init__()
        self._pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._pin, GPIO.OUT)

    def write(self, state: bool) -> None:
        """Write a state to the output

        Parameters
        ----------
        state : bool
            The state of the output

        Returns
        -------
        None
        """
        GPIO.output(self._pin, state)
