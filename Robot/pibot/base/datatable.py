from pibot.base.units import Distance, Angle

from pibot.base.pose import Pose2d, Pose3d
from pibot.base.rotation import Rotation2d, Rotation3d


class EntryType:
    """
    Different types for data table entries

    Attributes
    ----------
    NUMBER : int = 0
        A number
    BOOLEAN : int = 1
        A boolean
    TEXT : int = 2
        A string
    """

    NUMBER = 0
    BOOLEAN = 1
    TEXT = 2


class DataEntry:
    """
    An entry in a data table

    Attributes
    ----------
    entry_type : int
        The data type of the entry
    value : str
        The value of the entry
    """

    def __init__(self, entry_type: int, value: str):
        """Create a data table entry

        Parameters
        ----------
        entry_type : int
            The data type of the entry
        value : str
            The value of the entry

        Returns
        -------
        None
        """
        self.entry_type = entry_type
        self.value = value


class DataTable:
    """A table that handles robot data

    Attributes
    ----------
    entries : dict
        A dict of key, value pairs for each entry

    Methods
    -------
    put_number(key : str, value : float)
        Put a number in the table
    put_boolean(key : str, value : bool)
        Put a boolean in the table
    put_text(key : str, value : str)
        Put a string in the table
    get_number(key : str, default : float)
        Get a number from the table
    get_boolean(key : str, default : bool)
        Get a boolean from the table
    get_text(key : str, default : str)
        Get a string from the table
    put_pose2d(key : str, pose : Pose2d)
        Put a 2D pose in the table
    get_pose2d(key : str)
        get a 2D pose from the table
    put_pose3d(key : str, pose : Pose3d)
        Put a 3D pose in the table
    get_pose3d(key : str)
        get a 3D pose from the table

    """

    def __init__(self):
        """Create a data table

        Returns
        -------
        None
        """
        self.entries = {}

    def put_number(self, key: str, value: float) -> None:
        """Put a number in the table

        Parameters
        ----------
        key : str
            The key of the entry
        value : float
            The value of the entry

        Returns
        -------
        None
        """
        self.entries[key] = DataEntry(EntryType.NUMBER, str(value))

    def put_boolean(self, key: str, value: bool) -> None:
        """Put a boolean in the table

        Parameters
        ----------
        key : str
            The key of the entry
        value : bool
            The value of the entry

        Returns
        -------
        None
        """
        self.entries[key] = DataEntry(EntryType.BOOLEAN, "1" if value else "0")

    def put_text(self, key: str, value: str) -> None:
        """Put a string in the table

        Parameters
        ----------
        key : str
            The key of the entry
        value : str
            The value of the entry

        Returns
        -------
        None
        """
        self.entries[key] = DataEntry(EntryType.TEXT, value)

    def get_number(self, key: str, default: float = 0.0) -> float:
        """Get a number from the table

        Parameters
        ----------
        key : str
            The key of the entry
        default : float, optional
            The default value to return when failing

        Returns
        -------
        value : float
            The value of entry
        """
        if key not in self.entries:
            return default

        if self.entries[key].entry_type != EntryType.NUMBER:
            return default

        return self.entries[key].value

    def get_boolean(self, key: str, default: bool = False) -> bool:
        """Get a boolean from the table

        Parameters
        ----------
        key : str
            The key of the entry
        default : bool, optional
            The default value to return when failing

        Returns
        -------
        value : bool
            The value of entry
        """
        if key not in self.entries:
            return default

        if self.entries[key].entry_type != EntryType.BOOLEAN:
            return default

        return self.entries[key].value

    def get_text(self, key: str, default: str = "") -> str:
        """Get a string from the table

        Parameters
        ----------
        key : str
            The key of the entry
        default : str, optional
            The default value to return when failing

        Returns
        -------
        value : str
            The value of entry
        """
        if key not in self.entries:
            return default

        if self.entries[key].entry_type != EntryType.TEXT:
            return default

        return self.entries[key].value

    def put_pose2d(self, key: str, pose: Pose2d) -> None:
        """Put a 2D pose in the table

        Parameters
        ----------
        key : str
            The key of the entry
        pose : Pose2d
            The value of the entry

        Returns
        -------
        None
        """
        self.put_number(f"{key}.x", pose.get_x().get_meters())
        self.put_number(f"{key}.y", pose.get_y().get_meters())
        self.put_number(f"{key}.angle", pose.get_rotation().get_angle().get_radians())

    def get_pose2d(self, key: str) -> Pose2d:
        """Get a 2D pose from the table

        key : str
            The key of the entry

        Returns
        -------
        pose : Pose2d
            The value of entry
        """
        return Pose2d(
            Distance.from_meters(self.get_number(f"{key}.x")),
            Distance.from_meters(self.get_number(f"{key}.y")),
            Rotation2d(Angle.from_radians(self.get_number(f"{key}.angle"))),
        )

    def put_pose3d(self, key: str, pose: Pose3d) -> None:
        """Put a 3D pose in the table

        Parameters
        ----------
        key : str
            The key of the entry
        pose : Pose3d
            The value of the entry

        Returns
        -------
        None
        """
        self.put_number(f"{key}.x", pose.get_x().get_meters())
        self.put_number(f"{key}.y", pose.get_y().get_meters())
        self.put_number(f"{key}.z", pose.get_z().get_meters())
        self.put_number(f"{key}.pitch", pose.get_rotation().get_pitch().get_radians())
        self.put_number(f"{key}.roll", pose.get_rotation().get_roll().get_radians())
        self.put_number(f"{key}.yaw", pose.get_rotation().get_yaw().get_radians())

    def get_pose3d(self, key: str) -> Pose3d:
        """Get a 3D pose from the table

        key : str
            The key of the entry

        Returns
        -------
        pose : Pose3d
            The value of entry
        """
        return Pose3d(
            Distance.from_meters(self.get_number(f"{key}.x")),
            Distance.from_meters(self.get_number(f"{key}.y")),
            Distance.from_meters(self.get_number(f"{key}.z")),
            Rotation3d(
                Angle.from_radians(self.get_number(f"{key}.pitch")),
                Angle.from_radians(self.get_number(f"{key}.roll")),
                Angle.from_radians(self.get_number(f"{key}.yaw")),
            ),
        )
