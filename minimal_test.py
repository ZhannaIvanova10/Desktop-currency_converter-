import sys
from pathlib import Path

# Добавляем абсолютный путь к проекту
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

print(f"\nТекущий PYTHONPATH: {sys.path}\n")

try:
    # Проверяем импорт
    from src.utils.file_operations import read_json_file
    print("✅ Модуль успешно импортирован")
    
    # Проверяем чтение файла
    test_path = project_root / 'data' / 'test.json'
    print(f"\nПробуем прочитать: {test_path}")
    
    try:
        data = read_json_file(test_path)
        print(f"✅ Успех! Данные: {data}")
    except Exception as e:
        print(f"❌ Ошибка при чтении: {type(e).__name__}: {e}")
        raise

except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
    print("\nПроверьте:")
    print("1. Наличие __init__.py в src и src/utils")
    print("2. Регистр букв в именах файлов")
    print("3. Содержимое файлов")
