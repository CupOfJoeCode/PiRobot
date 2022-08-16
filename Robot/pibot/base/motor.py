class Motor:
    def __init__(self):
        self.speed = 0

    def set(self, speed):
        self.speed = min(1.0, max(-1.0, speed))

    def get(self):
        return self.speed

    def stop(self):
        self.set(0)
