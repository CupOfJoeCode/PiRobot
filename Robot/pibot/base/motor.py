class Motor:
    def __init__(self) -> None:
        self.speed = 0

    def set(self, speed: float) -> None:
        self.speed = min(1.0, max(-1.0, speed))

    def get(self) -> float:
        return self.speed

    def stop(self) -> None:
        self.set(0)
