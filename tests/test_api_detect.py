import numpy as np
import os
import pytest
from toy.api.detect import AtmosphericRiverAnalyzer, RiverTrendDetector

@pytest.fixture
def increasing_data():
    return np.load(os.path.join(os.path.dirname(__file__), "../data/test_data_increasing.npy"))

@pytest.fixture
def analyzer(increasing_data):
    return AtmosphericRiverAnalyzer(increasing_data)

@pytest.fixture
def detector(increasing_data):
    return RiverTrendDetector(increasing_data)

class TestAtmosphericRiverAnalyzer:
    def test_initialization(self, increasing_data):
        analyzer = AtmosphericRiverAnalyzer(increasing_data)
        assert isinstance(analyzer.data, np.ndarray)

    def test_calculate_intensity(self, analyzer):
        assert analyzer.calculate_intensity() == 2.0

class TestRiverTrendDetector:
    def test_initialization(self, increasing_data):
        detector = RiverTrendDetector(increasing_data)
        assert isinstance(detector.series, np.ndarray)

    @pytest.mark.parametrize("series,expected", [
        ([1, 2, 3], "increasing"),
        ([3, 2, 1], "decreasing")
    ])
    def test_detect_trend(self, series, expected):
        detector = RiverTrendDetector(series)
        assert detector.detect_trend() == expected
