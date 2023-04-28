from pibot.base.commands.command import Command


class Sequence(Command):
    def __init__(self, name, *cmds: Command) -> None:
        super().__init__(name)
        self.cmds = cmds
        self.cmd_index = 0

        def initialize_handler():
            self.cmd_index = 0
            self.cmds[0].initialize_handler()

        def execute_handler():
            current_command = self.cmds[self.cmd_index]
            current_command.execute_handler()
            if current_command.until_handler():
                current_command.end_handler()
                self.cmd_index += 1
                if self.cmd_index < len(self.cmds):
                    self.cmds[self.cmd_index].initialize_handler()

        def until_handler():
            return self.cmd_index >= len(self.cmds)

        def end_handler():
            if self.cmd_index < len(self.cmds):
                self.cmds[self.cmd_index].end_handler()
            self.cmd_index = -1

        self.initialize(initialize_handler).execute(execute_handler).until(
            until_handler
        ).end(end_handler)

    def __repr__(self) -> str:
        return f"Sequence({self.name}) {self.cmds}"
