class PID:
    def __init__(self, kP, kI, kD):
        self.kP = kP
        self.kI = kI
        self.kD = kD

        self.prev_error = 0.0
        self.total_error = 0.0

    def calculate(self, error):
        out_speed = (self.kP * error) + (self.kI * self.total_error) + \
            (self.kD * (error - self.prev_error))
        self.prev_error = error
        self.total_error += error
        return out_speed
