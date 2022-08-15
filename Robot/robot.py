class Robot:
    def __init__(self):
        self.data = {
            'Up': False,
            'Num': 0,
            'Text': 'Hello'
        }
        self.running = True

    def run(self):
        self.data['Stopped'] = False
        self.data['Num/pi'] = self.data['Num'] / 3.14159

    def stop(self):
        self.data['Stopped'] = True

    def trigger_start(self, trigger):
        if trigger == 'up':
            self.data['Up'] = True
        elif trigger == 'action':
            self.data['Num'] += 1

    def trigger_end(self, trigger):
        if trigger == 'up':
            self.data['Up'] = False

    def get_data(self):
        return self.data
