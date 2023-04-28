from time import sleep


class DigitalOutput:
    def __init__(self) -> None:
        self.state = False

    def write(self, state: bool) -> None:
        self.state = state

    def set(self) -> None:
        self.write(True)

    def reset(self) -> None:
        self.write(False)

    def pulse(self, time: float = 0.01, low: bool = False) -> None:
        self.write(True != low)
        sleep(time)
        self.write(False != low)
