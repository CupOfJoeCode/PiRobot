class PID:
    def __init__(self, kP: float, kI: float, kD: float) -> None:
        self.kP = kP
        self.kI = kI
        self.kD = kD

        self.prev_error = 0.0
        self.total_error = 0.0

    def calculate(self, error: float) -> float:
        out_speed = (
            (self.kP * error)
            + (self.kI * self.total_error)
            + (self.kD * (error - self.prev_error))
        )
        self.prev_error = error
        self.total_error += error
        return out_speed
