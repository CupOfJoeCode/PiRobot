class Robot:
    def __init__(self):
        self.data = {}
        self.running = True

    def run(self):
        pass

    def stop(self):
        # Stop all actuators
        pass

    def trigger_start(self, trigger):
        print(f'{trigger} Started')

    def trigger_end(self, trigger):
        print(f'{trigger} Ended')

    def get_data(self):
        return self.data
