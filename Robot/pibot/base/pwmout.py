class PWMOutput:
    """
    An oscillating output whose pulse with can be changed

    Attributes
    ----------
    width : float
        The pulse width in the range [0.0,1.0]

    Methods
    -------
    set(width : float)
        Set the pulse width
    """

    def __init__(self) -> None:
        """Create a new PWM output

        Returns
        -------
        None
        """
        self.width = 0

    def set(self, width: float) -> None:
        """Set the pulse width

        Parameters
        ----------
        width : float
            The pulse width in the range [0.0,1.0]

        Returns
        -------
        None
        """
        self.width = min(1.0, max(0.0, width))
