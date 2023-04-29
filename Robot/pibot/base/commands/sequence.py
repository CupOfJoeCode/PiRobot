from pibot.base.commands.command import Command


class Sequence(Command):
    """
    A command that contains a list of commands that run sequentially one after the other.
    Inherits from `Command`

    Methods
    -------
    __repr__()
        Returns a string representation of the command
    """

    def __init__(self, name, *cmds: Command) -> None:
        """Creates a sequence command

        Parameters
        ----------
        name : str
            The name of the command
        *cmds : Command
            A sequence of commands to be run sequentially

        Returns
        -------
        None
        """
        super().__init__(name)
        self._cmds = cmds
        self._cmd_index = 0

        def initialize_handler():
            self._cmd_index = 0
            self._cmds[0]._initialize_handler()

        def execute_handler():
            current_command = self._cmds[self._cmd_index]
            current_command._execute_handler()
            if current_command._until_handler():
                current_command._end_handler()
                self._cmd_index += 1
                if self._cmd_index < len(self._cmds):
                    self._cmds[self._cmd_index]._initialize_handler()

        def until_handler():
            return self._cmd_index >= len(self._cmds)

        def end_handler():
            if self._cmd_index < len(self._cmds):
                self._cmds[self._cmd_index]._end_handler()
            self._cmd_index = -1

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
        return f"Sequence({self.name}) {self._cmds}"
