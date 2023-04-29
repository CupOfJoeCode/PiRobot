from pibot.base.rotation import Rotation2d, Rotation3d
from pibot.base.vector import Vector
from pibot.base.units import Distance


class Pose2d:
    """
    A representation of where an object is in 2D space

    Methods
    -------
    get_x()
        Get the x position of the object
    get_y()
        Get the y position of the object
    get_rotation()
        Get the rotation of the object
    """

    def __init__(
        self,
        x: Distance = Distance(0),
        y: Distance = Distance(0),
        rotation: Rotation2d = Rotation2d(),
    ) -> None:
        """Create a 2D pose

        Parameters
        ----------
        x : Distance, optional
            The x position of the object
        y : Distance, optional
            The y position of the object
        rotation : Rotation2d, optional
            The rotation of the object

        Returns
        -------
        None
        """
        self._position = Vector(x.get_meters(), y.get_meters())
        self._rotation = rotation

    def get_x(self) -> Distance:
        """Get the x position of the object

        Returns
        -------
        x : Distance
            The x position of the object
        """
        return Distance.from_meters(self._position.x)

    def get_y(self) -> Distance:
        """Get the y position of the object

        Returns
        -------
        y : Distance
            The y position of the object
        """
        return Distance.from_meters(self._position.y)

    def get_rotation(self) -> Rotation2d:
        """Get the rotation of the object

        Returns
        -------
        rotation : Rotation2d
            The rotation of the object
        """
        return self._rotation


class Pose3d:
    """
    A representation of where an object is in 3D space

    Methods
    -------
    get_x()
        Get the x position of the object
    get_y()
        Get the y position of the object
    get_z()
        Get the z position of the object
    get_rotation()
        Get the rotation of the object
    """

    def __init__(
        self,
        x: Distance = Distance(0),
        y: Distance = Distance(0),
        z: Distance = Distance(0),
        rotation: Rotation3d = Rotation3d(),
    ) -> None:
        """Create a 3D pose

        Parameters
        ----------
        x : Distance, optional
            The x position of the object
        y : Distance, optional
            The y position of the object
        z : Distance, optional
            The z position of the object
        rotation : Rotation3d, optional
            The rotation of the object

        Returns
        -------
        None
        """
        self._position = Vector(x.get_meters(), y.get_meters(), z.get_meters())
        self._rotation = rotation

    def get_x(self) -> Distance:
        """Get the x position of the object

        Returns
        -------
        x : Distance
            The x position of the object
        """
        return Distance.from_meters(self._position.x)

    def get_y(self) -> Distance:
        """Get the y position of the object

        Returns
        -------
        y : Distance
            The y position of the object
        """
        return Distance.from_meters(self._position.y)

    def get_z(self) -> Distance:
        """Get the z position of the object

        Returns
        -------
        z : Distance
            The z position of the object
        """
        return Distance.from_meters(self._position.z)

    def get_rotation(self) -> Rotation3d:
        """Get the rotation of the object

        Returns
        -------
        rotation : Rotation3d
            The rotation of the object
        """
        return self._rotation

    def to_pose2d(self) -> Pose2d:
        """Project the pose down to 2D space

        Returns
        -------
        pose : Pose2d
            The 2D projected pose
        """
        return Pose2d(self.get_x(), self.get_y(), self._rotation.get_z())
