from unittest.mock import patch, mock_open
from src.utils import load_transactions

def test_load_transactions_valid():
    mock_data = '[{"id": 1, "amount": 100}]'
    with patch("builtins.open", mock_open(read_data=mock_data)):
        assert load_transactions("dummy.json") == [{"id": 1, "amount": 100}]

def test_load_transactions_invalid():
    with patch("builtins.open", side_effect=FileNotFoundError):
        assert load_transactions("nonexistent.json") == []