class Command:
    """
    An object representing an action. A command runs when scheduled and is interrupted when its condidiont is met.
    A command consists of four functions - initialize, execute, until, and end.
    initialize runs when the command first starts
    execute runs repeatedly until the command stops running
    until returns a condition that will interrupt the command when true
    end runs when the command ends or is interrupted

    ...

    Attributes
    ----------
    name : str
        the name of the command
    running : bool
        whether or not the command is currently running
    started : bool
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

        Returns
        -------
        None
        """
        self.name = name
        self._initialize_handler = lambda: None
        self._execute_handler = lambda: None
        self._until_handler = lambda: True
        self._end_handler = lambda: None
        self.running = True
        self.started = False

    def run(self) -> None:
        """Runs the command and calls one of the four handlers

        Returns
        -------
        None
        """
        if not self.running:
            return
        if not self.started:
            self.started = True
            self._initialize_handler()
            return
        self._execute_handler()
        if self._until_handler():
            self._end_handler()
            self.running = False

    def reset(self) -> None:
        """Resets the command

        Returns
        -------
        None
        """
        self.running = True
        self.started = False

    def stop(self) -> None:
        """Stops execution of the command

        Returns
        -------
        None
        """
        self.running = False
        self._end_handler()

    def initialize(self, handler: callable) -> None:
        """Sets the initialize handler and returns the command for function chaining

        Parameters
        ----------
        handler : callable
            The function to be called when the command is first run

        Returns
        -------
        self : Command
            The command for function chaining
        """
        self._initialize_handler = handler
        return self

    def execute(self, handler: callable):
        """Sets the execute handler and returns the command for function chaining

        Parameters
        ----------
        handler : callable
            The function to be called when the command is executing

        Returns
        -------
        self : Command
            The command for function chaining
        """
        self._execute_handler = handler
        return self

    def until(self, handler: callable):
        """Sets the until handler and returns the command for function chaining

        Parameters
        ----------
        handler : callable
            The function that returns True if the interrupting condition is met

        Returns
        -------
        self : Command
            The command for function chaining
        """
        self._until_handler = handler
        return self

    def end(self, handler: callable):
        """Sets the end handler and returns the command for function chaining

        Parameters
        ----------
        handler : callable
            The function to be called when the command ends

        Returns
        -------
        self : Command
            The command for function chaining
        """
        self._end_handler = handler
        return self

    def with_name(self, name: str):
        """Sets the name and returns the command for function chaining

        Parameters
        ----------
        name : str
            The name of the command

        Returns
        -------
        self : Command
            The command for function chaining
        """
        self.name = name
        return self

    def __repr__(self) -> str:
        """Returns a string representation of the command

        Returns
        -------
        repr : str
            A string representation of the command
        """
        return f"Command({self.name})"
