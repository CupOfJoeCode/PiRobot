from pibot.base.pwmout import PWMOutput
import RPi.GPIO as GPIO


class RpiPWMOutput(PWMOutput):
    """
    A PWM output connected to a Raspberry Pi.
    Inherits from `PWMOutput`

    Methods
    -------
    set(width : float)
        Set the pulse width of the output
    """

    def __init__(self, pin: int, freq: int = 100) -> None:
        """Create a Raspberry Pi PWM output

        Parameters
        ----------
        pin : int
            The output pin of the Raspberry Pi using the BCM number
        freq : int, optional
            The PWM frequency, in hertz

        Returns
        -------
        None
        """
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self.pwm = GPIO.PWM(pin, freq)
        self.pwm.start(0)

    def set(self, width: float) -> None:
        """Set the pulse width of the output

        Parameters
        ----------
        width : float
            The pulse width in the range [0.0,1.0]

        Returns
        -------
        None
        """
        self.pwm.ChangeDutyCycle(min(100, max(0, int(width * 100))))
