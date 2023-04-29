from pibot.base.datatable import DataTable


class BaseRobot:
    """
    The central robot that handles all functionality and data.

    Attributes
    ----------
    data : DataTable
        Robot data which can be accessed by other devices connected to the robot
    running : bool
        The state of if the robot is running

    Methods
    -------
    run()
        Gets called periodically when the robot is running
    stop()
        Gets called when the robot stops. Used to stop all actuators
    triggered(trigger : str)
        Checks if a trigger is currently active
    trigger_start(trigger : str)
        Activate a trigger
    trigger_end(trigger : str)
        Deactivate a trigger

    """

    def __init__(self) -> None:
        """Create a robot

        Returns
        -------
        None
        """
        self.data = DataTable()
        self.running = False

        self._triggers = {}

    def run(self) -> None:
        """Gets called periodically when the robot is running

        Returns
        -------
        None
        """
        pass

    def stop(self) -> None:
        """Gets called when the robot stops. Used to stop all actuators

        Returns
        -------
        None
        """
        pass

    def triggered(self, trigger: str) -> bool:
        """Checks if a trigger is currently active

        Parameters
        ----------
        trigger : str
            The name of the trigger

        Returns
        -------
        active : bool
            If the trigger is active
        """
        if trigger not in self._triggers:
            return False
        return self._triggers[trigger]

    def trigger_start(self, trigger: str) -> None:
        """Activate a trigger

        Parameters
        ----------
        trigger : str
            The name of the trigger

        Returns
        -------
        None
        """
        self._triggers[trigger] = True

    def trigger_end(self, trigger: str) -> None:
        """Deactivate a trigger

        Parameters
        ----------
        trigger : str
            The name of the trigger

        Returns
        -------
        None
        """
        self._triggers[trigger] = False
