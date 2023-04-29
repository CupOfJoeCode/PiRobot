class Motor:
    def __init__(self) -> None:
        self._speed = 0

    def set(self, speed: float) -> None:
        self._speed = min(1.0, max(-1.0, speed))

    def get(self) -> float:
        return self._speed

    def stop(self) -> None:
        self.set(0)
