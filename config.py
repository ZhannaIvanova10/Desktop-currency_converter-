# config.py
CURRENCY_RATES = {
    'USD': 75.0,
    'EUR': 85.0,
    'GBP': 95.0,  # Добавьте новые валюты
    'RUB': 1.0
}

LOG_CONFIG = {
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'level': 'DEBUG',
    'filename': 'logs/app.log'
}
