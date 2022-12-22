from pibot.base.commands.command import Command


class PrintCommand(Command):
    def __init__(self, message):
        super().__init__('Print')

        self.initialize(lambda: print(message))
