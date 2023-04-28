class PWMOutput:
    def __init__(self) -> None:
        self.width = 0

    def set(self, width: float) -> None:
        self.width = min(1.0, max(0.0, width))
