import os
import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(transaction):
    """Конвертирует сумму транзакции в рубли."""
    if not transaction or "amount" not in transaction or "currency" not in transaction:
        return None

    amount = transaction["amount"]
    currency = transaction["currency"]

    if currency == "RUB":
        return float(amount)

    if currency not in ("USD", "EUR"):
        return None

    try:
        response = requests.get(
            "https://api.apilayer.com/exchangerates_data/convert",
            params={"from": currency, "to": "RUB", "amount": amount},
            headers={"apikey": os.getenv("EXCHANGE_RATE_API_KEY")},
            timeout=10,
        )
        response.raise_for_status()
        return float(response.json()["result"])
    except (requests.RequestException, KeyError, ValueError) as e:
        print(f"Ошибка конвертации: {e}")
        return None
