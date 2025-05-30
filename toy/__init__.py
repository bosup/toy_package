# toy/__init__.py

__version__ = "0.1.0"

from toy.api.detect import AtmosphericRiverAnalyzer, RiverTrendDetector
from toy.api.statistics import RiverStatistics, RiverSummary
from toy.utils.ar_detection_utils import calculate_intensity, detect_trend
from toy.utils.ar_statistics_utils import get_max, summarize

__all__ = [
    "AtmosphericRiverAnalyzer",
    "RiverTrendDetector",
    "RiverStatistics",
    "RiverSummary",
    "calculate_intensity",
    "detect_trend",
    "get_max",
    "summarize",
]

