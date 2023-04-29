from pibot.base.units import Distance


class DistanceSensor:
    """
    A sensor that senses the distance to an object

    Methods
    -------
    get_distance()
        Get the distance to an object
    """

    def __init__(self) -> None:
        """Create a distance sensor

        Returns
        -------
        None
        """
        pass

    def get_distance(self) -> Distance:
        """Get the distance to an object

        Returns
        -------
        distance : Distance
            the distance to an object
        """
        return Distance(0)
