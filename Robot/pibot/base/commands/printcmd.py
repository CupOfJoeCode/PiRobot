from pibot.base.commands.command import Command


class PrintCommand(Command):
    """
    A command that prints a message.
    Inherits from `Command`
    """

    def __init__(self, message: str) -> None:
        """Creates a print command

        Parameters
        ----------
        message : str
            The message to be print

        Returns
        -------
        None
        """
        super().__init__("Print")

        self.initialize(lambda: print(message))
