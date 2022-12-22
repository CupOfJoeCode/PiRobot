from pibot.base.commands.command import Command


class Parallel(Command):
    def __init__(self, name, *cmds):
        super().__init__(name)
        self.cmds = cmds
        self.cmds_running = [False] * len(cmds)

        def initialize_handler():
            for index, cmd in enumerate(self.cmds):
                cmd.initialize_handler()
                self.cmds_running[index] = True

        def execute_handler():
            for index, cmd in enumerate(self.cmds):
                if self.cmds_running[index]:
                    cmd.execute_handler()
                    if cmd.until_handler():
                        cmd.end_handler()
                        self.cmds_running[index] = False

        def until_handler():
            return True not in self.cmds_running

        def end_handler():
            for index, cmd in enumerate(self.cmds):
                self.cmds_running[index] = False
                cmd.end_handler()

        self.initialize(initialize_handler).execute(
            execute_handler).until(until_handler).end(end_handler)
