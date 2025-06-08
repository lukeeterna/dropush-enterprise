import pytest
from src.ebay.client import EBayClient

def test_client_init():
    client = EBayClient('app123', 'cert456', 'tok789')
    assert client.app_id == 'app123'
    assert client.sandbox is True

def test_get_trending_products_returns_list():
    client = EBayClient('a','b','c')
    results = client.get_trending_products()
    assert isinstance(results, list)
