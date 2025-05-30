import numpy as np
from ..utils import get_max, summarize

class RiverStatistics:
    def __init__(self, data):
        self.data = np.array(data)

    def get_max(self):
        return get_max(self.data)

class RiverSummary:
    def __init__(self, data):
        self.data = np.array(data)

    def summarize(self):
        return summarize(self.data)
