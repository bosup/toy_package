import numpy as np
from typing import Sequence

def calculate_intensity(data: Sequence[float]) -> float:
    """
    Calculates the mean intensity from a sequence of data values.

    Parameters
    ----------
    data : array-like
        Input numerical data for intensity calculation.

    Returns
    -------
    float
        Mean value of the input data.
    """
    return float(np.mean(data))

def detect_trend(series: Sequence[float]) -> str:
    """
    Determines the trend of a numeric series.

    Parameters
    ----------
    series : array-like
        Input time series data.

    Returns
    -------
    str
        "increasing" if the series ends higher than it starts, otherwise "decreasing".
    """
    return "increasing" if series[-1] > series[0] else "decreasing"
