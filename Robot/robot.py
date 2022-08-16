

class Robot:
    def __init__(self):
        self.data = {
            'Num': 0
        }
        self.running = False

    def run(self):
        pass

    def stop(self):
        pass

    def trigger_start(self, trigger):
        if trigger == 'up':
            self.data['Num'] += 1
        elif trigger == 'down':
            self.data['Num'] -= 1

    def trigger_end(self, trigger):
        pass
