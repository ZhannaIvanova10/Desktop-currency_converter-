from unittest.mock import patch
from src.external_api import convert_to_rub

@patch("requests.get")
def test_convert_usd_to_rub(mock_get):
    mock_get.return_value.json.return_value = {"rates": {"RUB": 90.0}}
    transaction = {"amount": "100", "currency": "USD"}
    assert convert_to_rub(transaction) == 9000.0