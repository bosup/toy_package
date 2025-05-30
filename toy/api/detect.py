import numpy as np
from ..utils import calculate_intensity, detect_trend

class AtmosphericRiverAnalyzer:
    """
    Analyzes atmospheric river intensity based on input data.
    """

    def __init__(self, data):
        """
        Initializes the AtmosphericRiverAnalyzer with data.

        Parameters
        ----------
        data : array-like
            Input data representing intensity values.
        """
        self.data = np.array(data)

    def calculate_intensity(self):
        """
        Calculates the average intensity of the atmospheric river.

        Returns
        -------
        float
            Mean intensity value.
        """
        return calculate_intensity(self.data)


class RiverTrendDetector:
    """
    Detects trends in a given atmospheric river time series.
    """

    def __init__(self, series):
        """
        Initializes the RiverTrendDetector with a time series.

        Parameters
        ----------
        series : array-like
            Time series data for trend detection.
        """
        self.series = np.array(series)

    def detect_trend(self):
        """
        Detects if the time series trend is increasing or decreasing.

        Returns
        -------
        str
            "increasing" or "decreasing" based on trend direction.
        """
        return detect_trend(self.series)

