class PID:
    """
    A basic PID controller where

    ...

    Attributes
    ----------
    kP : float
        the proportional coefficient
    kI : float
        the integral coefficient
    kD : float
        the derivative coefficient

    Methods
    -------
    calculate(error : float)
        Calculate the output based on an input error
    """

    def __init__(self, kP: float, kI: float, kD: float) -> None:
        """Construct a PID controller

        Parameters
        ----------
        kP : float
            the proportional coefficient
        kI : float
            the integral coefficient
        kD : float
            the derivative coefficient

        Returns
        -------
        None
        """
        self.kP = kP
        self.kI = kI
        self.kD = kD

        self.prev_error = 0.0
        self.total_error = 0.0

    def calculate(self, error: float) -> float:
        """Construct a PID controller

        Parameters
        ----------
        kP : float
            the proportional coefficient
        kI : float
            the integral coefficient
        kD : float
            the derivative coefficient

        Returns
        -------
        output : float
            The output of the PID Controller
        """
        output = (
            (self.kP * error)
            + (self.kI * self.total_error)
            + (self.kD * (error - self.prev_error))
        )
        self.prev_error = error
        self.total_error += error
        return output
