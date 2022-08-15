class Robot:
    def __init__(self):
        self.data = {}

    def run(self):
        pass

    def trigger_start(self, trigger):
        print(f'{trigger} Started')

    def trigger_end(self, trigger):
        print(f'{trigger} Ended')

    def get_data(self):
        return self.data
