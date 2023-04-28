class Command:
    """
    An object representing an action. A command runs when scheduled and is interrupted when its condidiont is met.
    A command consists of four functions: `initialize`, `execute`, `until`, and `end`.
    `initialize` runs when the command first starts
    `execute` runs repeatedly until the command stops running
    `until` returns a condition that will interrupt the command when true
    `end` runs when the command ends or is interrupted

    ...

    Attributes
    ----------
    name : str
        the name of the command
    running : bool
        whether or not the command is currently running
    started: bool
        whether or not the command has been started

    Methods
    -------
    run()
        Runs the command and calls one of the four handlers
    reset()
        Resets the command
    stop()
        Stops execution of the command
    initialize(handler: callable)
        Sets the initialize handler and returns the command for function chaining
    execute(handler : callable)
        Sets the execute handler and returns the command for function chaining
    until(handler : callable)
        Sets the until handler and returns the command for function chaining
    end(handler : callable)
        Sets the end handler and returns the command for function chaining
    with_name(name : str)
        Sets the name and returns the command for function chaining
    __repr__()
        Returns a string representation of the command

    """

    def __init__(self, name) -> None:
        """Creates a command

        Parameters
        ----------
        name : str
            The name of the command
        """
        self.name = name
        self.initialize_handler = lambda: None
        self.execute_handler = lambda: None
        self.until_handler = lambda: True
        self.end_handler = lambda: None
        self.running = True
        self.started = False

    def run(self) -> None:
        """Runs the command and calls one of the four handlers"""
        if not self.running:
            return
        if not self.started:
            self.started = True
            self.initialize_handler()
            return
        self.execute_handler()
        if self.until_handler():
            self.end_handler()
            self.running = False

    def reset(self) -> None:
        """Resets the command"""
        self.running = True
        self.started = False

    def stop(self) -> None:
        """Stops execution of the command"""
        self.running = False
        self.end_handler()

    def initialize(self, handler: callable) -> None:
        """Sets the initialize handler and returns the command for function chaining

        Parameters
        ----------
        handler : callable
            The function to be called when the command is first run
        """
        self.initialize_handler = handler
        return self

    def execute(self, handler: callable):
        """Sets the execute handler and returns the command for function chaining

        Parameters
        ----------
        handler : callable
            The function to be called when the command is executing
        """
        self.execute_handler = handler
        return self

    def until(self, handler: callable):
        """Sets the until handler and returns the command for function chaining

        Parameters
        ----------
        handler : callable
            The function that returns True if the interrupting condition is met
        """
        self.until_handler = handler
        return self

    def end(self, handler: callable):
        """Sets the end handler and returns the command for function chaining

        Parameters
        ----------
        handler : callable
            The function to be called when the command ends
        """
        self.end_handler = handler
        return self

    def with_name(self, name: str):
        """Sets the name and returns the command for function chaining

        Parameters
        ----------
        name : str
            The name of the command
        """
        self.name = name
        return self

    def __repr__(self) -> str:
        """Returns a string representation of the command"""
        return f"Command({self.name})"
