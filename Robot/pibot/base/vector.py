import math


class Vector:

    """
    A 1-4 component vector

    ...

    Attributes
    ----------
    x : float
        the x component
    y : float
        the y component
    z : float
        the z component
    w : float
        the w component


    Methods
    -------
    from_color(color : tuple[int])
        Construct a 3 component vector from a color
    length()
        Get the magnitude of the vector
    normalize()
        Return the vector normalized as a unit vector
    dot(other : Vector)
        Return the dot product of the vector and another vector
    to_color()
        Return a color from the vector
    __add__(other : Vector)
        Return the sum of the vector and another vector
    __sub__(other : Vector)
        Return the difference of the vector and another vector
    __mul__(other : float)
        Return the product of the vector multiplied by a scalar

    """

    def __init__(self, x: float = 0, y: float = 0, z: float = 0, w: float = 0) -> None:
        """Construct a vector

        Parameters
        ----------
        x : float, optional
            The x component
        y : float, optional
            The y component
        z : float, optional
            The z component
        w : float, optional
            The w component

        Returns
        -------
        None
        """
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    @classmethod
    def from_color(color: tuple[int]):
        """Construct a 3 component vector from a color

        Parameters
        ----------
        color : tuple[int]
            A 3-element tuple with integers from [0,255] representing R,G,B

        Returns
        -------
        vector : Vector
            A vector from the color information
        """
        return Vector(color[0] / 255.0, color[1] / 255.0, color[2] / 255.0)

    def length(self) -> float:
        """Get the magnitude of the vector

        Returns
        -------
        length : float
            The magnitude of the vector
        """
        return math.sqrt((self.x**2) + (self.y**2) + (self.z**2) + (self.w**2))

    def normalize(self):
        """Return the vector normalized as a unit vector

        Returns
        -------
        vector : Vector
            The normalized vector
        """
        return self * (1 / self.length())

    def dot(self, other) -> float:
        """Return the dot product of the vector and another vector

        Parameters
        ----------
        other : Vector
            The other vector

        Returns
        -------
        product : float
            The dot product of the two vectors
        """
        return self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w

    def to_color(self) -> tuple[int]:
        """Return a color from the vector

        Returns
        -------
        color : tuple[int]
            A 3-element tuple with integers from [0,255] representing R,G,B
        """
        return tuple(min(255, max(0, int(x * 255))) for x in [self.x, self.y, self.z])

    def __add__(self, other):
        """Return the sum of the vector and another vector

        Parameters
        ----------
        other : Vector
            The other vector

        Returns
        -------
        sum : Vector
            The sum of the two vectors
        """
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """Return the difference of the vector and another vector

        Parameters
        ----------
        other : Vector
            The other vector

        Returns
        -------
        difference : Vector
            The difference of the two vectors
        """
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: float):
        """Return the product of the vector multiplied by a scalar
        Parameters
        ----------
        other : float
            The scalar

        Returns
        -----
        product : Vector
            The product of the vector and scalar
        """
        return Vector(self.x * other, self.y * other, self.z * other)
