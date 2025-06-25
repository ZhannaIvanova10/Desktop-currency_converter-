import os
import requests
from typing import Dict, Optional, Any
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/latest"

def convert_to_rub(transaction: Dict[str, Any]) -> Optional[float]:
    """Конвертирует сумму транзакции в рубли."""
    if not transaction or "amount" not in transaction or "currency" not in transaction:
        return None
        
    amount = float(transaction["amount"])
    currency = transaction["currency"]
    
    if currency == "RUB":
        return amount
        
    if currency not in ("USD", "EUR"):
        return None
    
    try:
        response = requests.get(
            BASE_URL,
            params={"base": currency, "symbols": "RUB"},
            headers={"apikey": API_KEY},
            timeout=10
        )
        response.raise_for_status()
        rate = response.json()["rates"]["RUB"]
        return amount * rate
    except (requests.RequestException, KeyError, ValueError):
        return None
