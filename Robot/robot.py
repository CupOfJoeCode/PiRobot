from pibot.rpipwm import RpiPWMOutput


class Robot:
    def __init__(self):
        self.data = {}
        self.running = True

    def run(self):
        pass

    def stop(self):
        pass

    def trigger_start(self, trigger):
        pass

    def trigger_end(self, trigger):
        pass
