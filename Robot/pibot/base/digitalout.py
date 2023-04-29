from time import sleep
from pibot.base.units import Time


class DigitalOutput:
    """
    An output that writes a boolean value

    ...

    Attributes
    ----------
    state : bool
        the current state of the output

    Methods
    -------
    write(state : bool)
        Write a value to the output
    set()
        Turn the output on
    reset()
        Turn the output off
    pulse(time : Time, low : bool)
        Pulse the output for a specified amount of time
    """

    def __init__(self) -> None:
        """Creates a digital output

        Returns
        -------
        None
        """
        self.state = False

    def write(self, state: bool) -> None:
        """Write a value to the output

        Parameters
        ----------
        state : bool
            The value to write to the output

        Returns
        -------
        None
        """
        self.state = state

    def set(self) -> None:
        """Turn the output on

        Returns
        -------
        None
        """
        self.write(True)

    def reset(self) -> None:
        """Turn the output off

        Returns
        -------
        None
        """
        self.write(False)

    def pulse(self, time: Time = Time.from_milliseconds(10), low: bool = False) -> None:
        """Pulse the output for a specified amount of time

        Parameters
        ----------
        time : Time, optional
            How long the pulse should last
        low : bool, optional
            Whether it should pulse low instead of high

        Returns
        -------
        None
        """
        self.write(True != low)
        sleep(time.get_seconds())
        self.write(False != low)
