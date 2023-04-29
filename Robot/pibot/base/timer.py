import time
from pibot.base.units import Time


class Timer:
    def __init__(self) -> None:
        self._initial_time = time.time()

    def start(self) -> None:
        self._initial_time = time.time()

    def get_time(self) -> Time:
        return Time.from_seconds(time.time() - self._initial_time)
