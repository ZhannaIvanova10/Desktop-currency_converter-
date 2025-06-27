"""Utilities module for file operations."""

import json
import logging
from pathlib import Path
from typing import List, Dict, Union


logger = logging.getLogger(__name__)


def read_json_file(file_path: Union[str, Path]) -> List[Dict]:
    """Чтение JSON файла с транзакциями."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.info("Успешно прочитан файл: %s", file_path)
            return data
    except Exception as e:
        logger.error(
            "Ошибка чтения файла %s: %s",
            file_path,
            str(e),
            exc_info=True)
        raise
