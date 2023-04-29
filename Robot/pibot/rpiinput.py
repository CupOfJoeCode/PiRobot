from pibot.base.digitalin import DigitalInput
import RPi.GPIO as GPIO


class RpiInput(DigitalInput):
    """
    A digital input connected to a Raspberry Pi.
    Inherits from `DigitalInput`

    Methods
    -------
    get()
        Get the state of the input
    """

    def __init__(self, pin: int) -> None:
        """Create a Raspberry Pi digital input

        Parameters
        ----------
        pin : int
            The input pin of the Raspberry Pi using the BCM number

        Returns
        -------
        None
        """
        super().__init__()
        self._pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._pin, GPIO.IN)

    def get(self) -> bool:
        """Get the state of the input

        Returns
        -------
        input : bool
            The state of the input
        """
        return bool(GPIO.input(self._pin))
