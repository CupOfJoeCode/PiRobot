from pibot.base.commands.command import Command
from pibot.base.timer import Timer
from pibot.base.units import Time


class Wait(Command):
    """
    A command that ends after a specified amount of time.
    Inherits from `Command`
    """

    def __init__(self, duration: Time) -> None:
        """Creates a print command

        Parameters
        ----------
        duration : Time
            How long the command will run for before ending

        Returns
        -------
        None
        """
        super().__init__(f"Wait {round(duration.get_seconds(),2)}")
        self.duration = duration.get_seconds()
        self.timer = Timer()

        def initialize_handler():
            self.timer.start()

        def until_handler():
            return self.timer.get_time().get_seconds() >= self.duration

        self.initialize(initialize_handler).until(until_handler)
