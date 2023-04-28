import time


class Timer:
    def __init__(self) -> None:
        self.initial_time = time.time()

    def start(self) -> None:
        self.initial_time = time.time()

    def get_seconds(self) -> float:
        return time.time() - self.initial_time
