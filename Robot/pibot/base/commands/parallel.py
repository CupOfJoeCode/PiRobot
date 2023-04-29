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

        Returns
        -------
        None
        """
        super().__init__(name)
        self._cmds = cmds
        self._cmds_running = [False] * len(cmds)

        def initialize_handler():
            for index, cmd in enumerate(self._cmds):
                cmd._initialize_handler()
                self._cmds_running[index] = True

        def execute_handler():
            for index, cmd in enumerate(self._cmds):
                if self._cmds_running[index]:
                    cmd._execute_handler()
                    if cmd._until_handler():
                        cmd._end_handler()
                        self._cmds_running[index] = False

        def until_handler():
            return True not in self._cmds_running

        def end_handler():
            for index, cmd in enumerate(self._cmds):
                self._cmds_running[index] = False
                cmd._end_handler()

        self.initialize(initialize_handler).execute(execute_handler).until(
            until_handler
        ).end(end_handler)

    def __repr__(self) -> str:
        """Returns a string representation of the command

        Returns
        -------
        repr : str
            A string representation of the command
        """
        return f"Parallel({self.name}) {self._cmds}"
