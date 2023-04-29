from pibot.base.motor import Motor
from pibot.rpipwm import RpiPWMOutput


class RpiHBridge(Motor):
    """
    An motor controller for an h-bridge motor driver

    Methods
    -------
    set(speed : float)
        Set the speed of the motor
    stop()
        Stop the motor
    get()
        Get the speed of the motor
    """

    def __init__(
        self, pin0: int, pin1: int, inverted: bool = False, pwm_freq: int = 100
    ) -> None:
        """Create a Raspberry Pi H-Bridge controller

        Parameters
        ----------
        pin0 : int
            The first output pin using the BCM number
        pin1 : int
            The seconds output pin using the BCM number
        inverted : bool, optional
            Invert the motor
        pwm_freq : int, optional
            The PWM frequency, in hertz

        Returns
        -------
        None
        """
        super().__init__()
        self._pwm0 = RpiPWMOutput(pin0, pwm_freq)
        self._pwm1 = RpiPWMOutput(pin1, pwm_freq)
        self._speed = 0
        self._pwm0.set(0)
        self._pwm1.set(0)
        self._inverted = inverted

    def set(self, speed: float) -> None:
        """Set the speed of the motor

        Parameters
        ----------
        speed : float
            The speed of the motor in the range [-1.0,1.0] 1.0 being full speed and -1.0 being full speed reversed

        Returns
        -------
        None
        """
        clamped = max(-1, min(1, speed))
        realSpeed = clamped * 0.5 + 0.5
        if self._inverted:
            realSpeed = 1 - realSpeed
        self._pwm1.set(realSpeed)
        self._pwm0.set(1.0 - realSpeed)
        self._speed = clamped

    def stop(self) -> None:
        """Stop the motor

        Returns
        -------
        None
        """
        self._pwm0.set(0)
        self._pwm1.set(0)
        self._speed = 0

    def get(self) -> float:
        """Get the speed of the motor

        Returns
        -------
        speed : float
            The speed of the motor
        """
        return self._speed
