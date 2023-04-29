import math
from pibot.base.units import Angle
from pibot.base.vector import Vector


class Rotation2d:
    """A rotation in 2D space that can be used to rotate a vector around the z axis

    Methods
    -------
    get_angle()
        Get the angle of rotation
    get_sin()
        Get the sine of the angle
    get_cos()
        Get the cosine of the angle
    get_tan()
        Get the tangent of the angle
    get_cot()
        Get the cotangent of the angle
    rotate(vector : Vector)
        Rotate a vector around the z axis
    """

    def __init__(self, angle: Angle = Angle(0)) -> None:
        """Create a 2D rotation

        Parameters
        ----------
        angle : Angle, optional
            The angle of the rotation

        Returns
        -------
        None
        """
        self._angle = angle

    def get_angle(self) -> Angle:
        """Get the angle of rotation

        Returns
        -------
        angle : Angle
            The angle of rotation
        """
        return self._angle

    def get_sin(self) -> float:
        """Get the sine of the angle

        Returns
        -------
        sin : float
            The sine of the angle
        """
        return math.sin(self._angle.get_radians())

    def get_cos(self) -> float:
        """Get the cosine of the angle

        Returns
        -------
        cos : float
            The cosine of the angle
        """
        return math.cos(self._angle.get_radians())

    def get_tan(self) -> float:
        """Get the tangent of the angle

        Returns
        -------
        tan : float
            The tangent of the angle
        """
        return math.tan(self._angle.get_radians())

    def get_cot(self) -> float:
        """Get the cotangent of the angle

        Returns
        -------
        cot : float
            The cotangent of the angle
        """
        return math.tan(self._angle.get_radians())

    def rotate(self, vector: Vector) -> Vector:
        """Rotate a vector around the z axis

        Parameters
        ----------
        vector : Vector
            The vector to be rotated

        Returns
        -------
        rotated : Vector
            The rotated vector
        """
        s = self.get_sin()
        c = self.get_cos()
        return Vector(vector.x * c - vector.y * s, vector.x * s + vector.y * c)


class Rotation3d:
    """A rotation in 3D space that can be used to rotate a vector using Euler angles

    Methods
    -------
    get_x()
        Get the pitch/angle of rotation around the x-axis
    get_y()
        Get the roll/angle of rotation around the y-axis
    get_z()
        Get the yaw/angle of rotation around the z-axis
    get_pitch()
        Get the pitch/angle of rotation around the x-axis
    get_roll()
        Get the roll/angle of rotation around the y-axis
    get_yaw()
        Get the yaw/angle of rotation around the z-axis
    rotate(vector : Vector)
        Rotate a vector around the origin with the order of pitch, roll, yaw

    """

    def __init__(
        self,
        pitch: Angle = Angle(0),
        roll: Angle = Angle(0),
        yaw: Angle = Angle(0),
    ) -> None:
        """Create a 3D rotation

        Parameters
        ----------
        pitch : Angle, optional
            The rotation around the x-axis
        roll : Angle, optional
            The rotation around the y-axis
        yaw : Angle, optional
            The rotation around the z-axis

        Returns
        -------
        None
        """
        self._pitch = Rotation2d(pitch)
        self._roll = Rotation2d(roll)
        self._yaw = Rotation2d(yaw)

    def get_x(self) -> Angle:
        """Get the pitch/angle of rotation around the x-axis

        Returns
        -------
        angle : Angle
            The pitch/angle of rotation around the x-axis
        """
        return self._pitch.get_angle()

    def get_y(self) -> Angle:
        """Get the roll/angle of rotation around the y-axis

        Returns
        -------
        angle : Angle
            The roll/angle of rotation around the y-axis
        """
        return self._roll.get_angle()

    def get_z(self) -> Angle:
        """Get the yaw/angle of rotation around the z-axis

        Returns
        -------
        angle : Angle
            The yaw/angle of rotation around the z-axis
        """
        return self._yaw.get_angle()

    def get_pitch(self) -> Angle:
        """Get the pitch/angle of rotation around the x-axis

        Returns
        -------
        angle : Angle
            The pitch/angle of rotation around the x-axis
        """
        return self.get_x()

    def get_roll(self) -> Angle:
        """Get the roll/angle of rotation around the y-axis

        Returns
        -------
        angle : Angle
            The roll/angle of rotation around the y-axis
        """
        return self.get_y()

    def get_yaw(self) -> Angle:
        """Get the yaw/angle of rotation around the z-axis

        Returns
        -------
        angle : Angle
            The yaw/angle of rotation around the z-axis
        """
        return self.get_z()

    def rotate(self, vector: Vector) -> Vector:
        """Rotate a vector around the origin with the order of pitch, roll, yaw

        Parameters
        ----------
        vector : Vector
            The vector to be rotated

        Returns
        -------
        rotated : Vector
            The rotated vector
        """
        v = vector
        x_rot = self._pitch.rotate(Vector(v.y, v.z))
        v = Vector(v.x, x_rot.x, x_rot.y)
        y_rot = self._roll.rotate(Vector(v.x, v.z))
        v = Vector(y_rot.x, v.y, y_rot.y)
        z_rot = self._roll.rotate(Vector(v.x, v.y))
        return Vector(z_rot.x, z_rot.y, v.z)
