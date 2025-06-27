import sys
import os
import logging
from pathlib import Path

# Настройка логгирования для диагностики
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('debug')

# Выводим системную информацию
logger.info("\n=== СИСТЕМНАЯ ИНФОРМАЦИЯ ===")
logger.info(f"Python path: {sys.path}")
logger.info(f"Current directory: {os.getcwd()}")

# Добавляем текущую директорию в PYTHONPATH
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
logger.info(f"\nAdded to PYTHONPATH: {project_root}")

try:
    logger.info("\n=== ПРОВЕРКА ИМПОРТА ===")
    from src.utils.file_operations import read_json_file
    logger.info("✅ Модуль file_operations успешно импортирован")
    
    # Проверяем путь к тестовому файлу
    test_file = project_root / 'data' / 'test.json'
    logger.info(f"\n=== ПРОВЕРКА ФАЙЛА {test_file} ===")
    
    if not test_file.exists():
        logger.error(f"❌ Файл не существует: {test_file}")
    else:
        logger.info("✅ Файл существует")
        logger.info("Содержимое файла:")
        with open(test_file, 'r') as f:
            logger.info(f.read())
        
        # Пробуем прочитать через функцию
        logger.info("\n=== ТЕСТ ФУНКЦИИ read_json_file ===")
        try:
            data = read_json_file(test_file)
            logger.info(f"✅ Успешно! Полученные данные: {data}")
        except Exception as e:
            logger.error(f"❌ Ошибка при чтении: {type(e).__name__}: {e}", exc_info=True)

except ImportError as e:
    logger.error(f"❌ Ошибка импорта: {e}")
    logger.info("\nСодержимое папки src/utils:")
    logger.info(os.listdir(project_root / 'src' / 'utils'))
