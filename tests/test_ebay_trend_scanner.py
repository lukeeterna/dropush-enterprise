import pytest
from src.analytics.ebay_trend_scanner import TrendScanner

class DummyClient:
    pass

def test_trend_scanner_init():
    scanner = TrendScanner(DummyClient())
    assert hasattr(scanner, 'fetch_trends')
    assert callable(scanner.fetch_trends)
