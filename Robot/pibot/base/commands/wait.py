from pibot.base.commands.command import Command
from pibot.base.timer import Timer


class Wait(Command):
    def __init__(self, duration_seconds: float) -> None:
        super().__init__(f"Wait {duration_seconds}")
        self.duration = duration_seconds
        self.timer = Timer()

        def initialize_handler():
            self.timer.start()

        def until_handler():
            return self.timer.get_seconds() >= self.duration

        self.initialize(initialize_handler).until(until_handler)
