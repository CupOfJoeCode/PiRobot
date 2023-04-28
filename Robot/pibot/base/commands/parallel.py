from pibot.base.commands.command import Command


class Parallel(Command):
    """
    A command that contains a list of commands that all run at the same time in parallel.
    Inherits from `Command`

    Methods
    -------
    __repr__()
        Returns a string representation of the command
    """

    def __init__(self, name, *cmds: Command) -> None:
        """Creates a parallel command

        Parameters
        ----------
        name : str
            The name of the command
        *cmds : Command
            A sequence of commands to be run in parallel
        """
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

        self.initialize(initialize_handler).execute(execute_handler).until(
            until_handler
        ).end(end_handler)

    def __repr__(self) -> str:
        """Returns a string representation of the command"""
        return f"Parallel({self.name}) {self.cmds}"
