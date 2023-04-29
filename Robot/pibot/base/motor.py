class Motor:
    """
    A motor

    Methods
    -------
    set(speed : float)
        Set the speed of the motor
    get()
        Get the speed of the motor
    stop()
        Stop the motor
    """

    def __init__(self) -> None:
        """Create a motor

        Returns
        -------
        None
        """
        self._speed = 0

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
        self._speed = min(1.0, max(-1.0, speed))

    def get(self) -> float:
        """Get the speed of the motor

        Returns
        -------
        speed : float
            The speed of the motor
        """
        return self._speed

    def stop(self) -> None:
        """Stop the motor

        Returns
        -------
        None
        """
        self.set(0)
