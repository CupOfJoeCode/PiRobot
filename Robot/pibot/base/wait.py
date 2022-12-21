from pibot.base.command import Command
from pibot.base.timer import Timer


class Wait(Command):

    def __init__(self, delay_seconds):
        super().__init__(f'Wait {delay_seconds}')
        self.delay = delay_seconds
        self.timer = Timer()

    def initialize_handler(self):
        self.timer.start()

    def until_handler(self):
        return self.timer.get_seconds() >= self.delay_seconds
