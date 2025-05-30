import numpy as np
from typing import Sequence, Dict, Union

def get_max(data: Sequence[float]) -> float:
    """Return the maximum value from the data sequence."""
    return float(np.max(data))

def summarize(data: Sequence[float]) -> Dict[str, Union[float, int]]:
    """Summarize the data with mean and count."""
    return {"mean": float(np.mean(data)), "count": len(data)}
