import json
from typing import List, Dict


def load_transactions(file_path: str) -> List[Dict]:
    """Загружает транзакции из JSON-файла и возвращает список словарей."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
