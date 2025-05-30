import numpy as np
import os
import pytest
from toy.api.statistics import RiverStatistics, RiverSummary

@pytest.fixture
def increasing_data():
    return np.load(os.path.join(os.path.dirname(__file__), "../data/test_data_increasing.npy"))

@pytest.fixture
def stats(increasing_data):
    return RiverStatistics(increasing_data)

@pytest.fixture
def summary(increasing_data):
    return RiverSummary(increasing_data)

class TestRiverStatistics:
    def test_initialization(self, increasing_data):
        stats = RiverStatistics(increasing_data)
        assert isinstance(stats.data, np.ndarray)

    def test_get_max(self, stats):
        assert stats.get_max() == 3.0

class TestRiverSummary:
    def test_initialization(self, increasing_data):
        summary = RiverSummary(increasing_data)
        assert isinstance(summary.data, np.ndarray)

    def test_summarize(self, summary):
        result = summary.summarize()
        assert result["mean"] == 2.0
        assert result["count"] == 3
