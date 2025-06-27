from .log_config import setup_logging

# Инициализация логгеров для всех модулей
utils_logger = setup_logging("utils", "utils.log")
masks_logger = setup_logging("masks", "masks.log")
