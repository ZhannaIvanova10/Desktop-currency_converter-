import os
import requests
from dotenv import load_dotenv


load_dotenv()


def convert_to_rub(transaction: dict) -> float:
    """Конвертирует сумму транзакции в рубли по текущему курсу."""
    amount = transaction["amount"]
    currency = transaction.get("currency", "RUB").upper()

    if currency == "RUB":
        return float(amount)

    api_key = os.getenv("API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/" f"latest?base={currency}"
    response = requests.get(
        url, headers={"apikey": api_key}  # Исправлено: добавлен пробел после :
    )
    response.raise_for_status()

    rate = response.json()["rates"]["RUB"]
    return float(amount) * rate


# Добавлена эта пустая строка в конце файла
