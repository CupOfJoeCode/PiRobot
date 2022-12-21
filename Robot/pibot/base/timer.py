import time


class Timer:
    def __init__(self):
        self.initial_time = time.time()

    def start(self):
        self.initial_time = time.time()

    def get_seconds(self):
        return time.time() - self.initial_time
