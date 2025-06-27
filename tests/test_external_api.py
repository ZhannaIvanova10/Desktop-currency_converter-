import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


from src.external_api import convert_to_rub
from unittest.mock import patch, MagicMock

def test_convert_usd_to_rub():
    with patch('src.external_api.requests.get') as mock_get:
        mock_response=MagicMock()
        mock_response.json.return_value={'success': True, 'result': 7500.0}
        mock_get.return_value=mock_response

        transaction={'amount': 100, 'currency': 'USD'}
        result=convert_to_rub(transaction)
        assert result == 7500.0

def test_convert_eur_to_rub():
    with patch('src.external_api.requests.get') as mock_get:
        mock_response=MagicMock()
        mock_response.json.return_value={'success': True, 'result': 8500.0}
        mock_get.return_value=mock_response

        transaction={'amount': 100, 'currency': 'EUR'}
        result=convert_to_rub(transaction)
        assert result == 8500.0

def test_already_in_rub():
    transaction={'amount': 1000, 'currency': 'RUB'}
    result=convert_to_rub(transaction)
    assert result == 1000.0

def test_invalid_currency():
    transaction={'amount': 100, 'currency': 'GBP'}
    result=convert_to_rub(transaction)
    assert result is None

def test_invalid_transaction():
    assert convert_to_rub({}) is None
    assert convert_to_rub({'amount': 100}) is None
    assert convert_to_rub({'currency': 'USD'}) is None
