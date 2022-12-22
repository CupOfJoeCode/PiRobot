class Command:
    def __init__(self, name):
        self.name = name
        self.initialize_handler = lambda: None
        self.execute_handler = lambda: None
        self.until_handler = lambda: True
        self.end_handler = lambda: None
        self.running = True
        self.started = False

    def run(self):
        if not self.running:
            return
        if not self.started:
            self.started = True
            return self.initialize_handler()
        self.execute_handler()
        if self.until_handler():
            self.end_handler()
            self.running = False

    def reset(self):
        self.running = True
        self.started = False

    def stop(self):
        self.running = False
        self.end_handler()

    def initialize(self, handler):
        self.initialize_handler = handler
        return self

    def execute(self, handler):
        self.execute_handler = handler
        return self

    def until(self, handler):
        self.until_handler = handler
        return self

    def end(self, handler):
        self.end_handler = handler
        return self

    def with_name(self, name):
        self.name = name
        return self

    def __repr__(self):
        return f'Command({self.name})'
