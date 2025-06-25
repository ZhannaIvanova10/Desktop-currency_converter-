from src.utils import read_json_file
from src.external_api import convert_currency_to_rub  # Исправлено имя функции


def main():
    transactions = read_json_file("data/operations.json")
    print(f"Найдено транзакций: {len(transactions)}")

    for transaction in transactions:
        amount_in_rub = convert_currency_to_rub(transaction)  # Исправлено имя функции
        currency = transaction.get("currency", "UNKNOWN")
        amount = transaction.get("amount", "N/A")
        transaction_id = transaction.get("id", "N/A")
        print(f"Транзакция {transaction_id}: {amount} {currency} = {amount_in_rub} RUB")


if __name__ == "__main__":
    main()
