class LowPassFilter:
    """
    A simple multi-pole IIR low-pass filter

    ...

    Attributes
    ----------
    cutoff : float
        the cutoff of the filter in the range [0.0,1.0] from fully closed to fully open

    Methods
    -------
    set_cutoff(cutoff : float)
        Set the cutoff of the filter

    get_cutoff()
        Get the filter's current cutoff

    calculate(sample : float)
        Calculate the filter's output based on an input sample
    """

    def __init__(self, cutoff: float, poles: int = 1) -> None:
        """Construct a low-pass filter

        Parameters
        ----------
        cutoff : float
            the cutoff of the filter in the range [0.0,1.0] from fully closed to fully open
        poles : int, optional
            the number of poles of the filter

        Returns
        -------
        None
        """
        self._buffers = [0] * poles
        self._cutoff = min(1.0, max(0.0, cutoff))

    def set_cutoff(self, cutoff: float) -> None:
        """Set the cutoff of the filter

        Parameters
        ----------
        cutoff : float
            the cutoff of the filter in the range [0.0,1.0] from fully closed to fully open

        Returns
        -------
        None
        """
        self._cutoff = min(1.0, max(0.0, cutoff))

    def get_cutoff(self) -> float:
        """Get the filter's current cutoff

        Returns
        -------
        cutoff : float
            The cutoff of the filter
        """
        return self._cutoff

    def calculate(self, sample: float) -> float:
        """Calculate the filter's output based on an input sample

        Parameters
        ----------
        sample : float
            The input sample of the first filter pole

        Returns
        -------
        output : float
            The output of the last filter pole
        """
        for index, buf in enumerate(self._buffers):
            if index == 0:
                prev_buf = sample
            else:
                prev_buf = self._buffers[index - 1]

            self._buffers[index] += self._cutoff * (prev_buf - buf)
        return self._buffers[-1]
