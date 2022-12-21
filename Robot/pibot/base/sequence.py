from pibot.base.command import Command


class Sequence(Command):
    def __init__(self, name, *cmds):
        super().__init__(name)
        self.cmds = cmds
        self.cmd_index = 0

    def initialize_handler(self):
        self.cmd_index = 0
        self.cmds[0].initialize_handler()

    def execute_handler(self):
        current_command = self.cmds[self.cmd_index]
        current_command.execute_handler()
        if current_command.until_handler():
            current_command.end_handler()
            self.cmd_index += 1
            if self.cmd_index < len(self.cmds):
                self.cmds[self.cmd_index].initialize_handler()

    def until_handler(self):
        return self.cmd_index >= len(self.cmds)

    def end_handler(self):
        self.cmds[self.cmd_index].end_handler()
        self.cmd_index = -1
