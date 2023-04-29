import time
from pibot.base.units import Time


class Timer:
    """
    A way to keep track of elapsed time

    Methods
    -------
    start()
        Start the timer
    get_time()
        Get the elapsed time since the timer was started
    """

    def __init__(self) -> None:
        """Create a timer

        Returns
        -------
        None
        """
        self._initial_time = time.time()

    def start(self) -> None:
        """Start the timer

        Returns
        -------
        None
        """
        self._initial_time = time.time()

    def get_time(self) -> Time:
        """Get the elapsed time since the timer was started

        Returns
        -------
        time : Time
            The elapsed time since the timer was started
        """
        return Time.from_seconds(time.time() - self._initial_time)
