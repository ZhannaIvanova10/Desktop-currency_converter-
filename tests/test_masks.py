"""
Тесты для модуля masks.account_masks
Проверка функций маскирования банковских реквизитов
"""

import pytest
from src.masks import mask_card, mask_account


class TestMaskCard:
    """Тесты для функции mask_card"""

    def test_valid_card(self):
        """Проверка маскировки валидного номера карты"""
        assert mask_card("1234567812345678") == "1234 56** **** 5678"
        assert mask_card("1111222233334444") == "1111 22** **** 4444"

    def test_short_card(self):
        """Проверка обработки слишком короткого номера"""
        assert mask_card("12345678") is None

    def test_non_digit(self):
        """Проверка обработки нечисловых символов"""
        assert mask_card("1234abcd5678efgh") is None

    def test_empty_input(self):
        """Проверка обработки пустой строки"""
        assert mask_card("") is None


class TestMaskAccount:
    """Тесты для функции mask_account"""

    def test_valid_account(self):
        """Проверка маскировки валидного номера счета"""
        assert mask_account("12345678") == "**5678"
        assert mask_account("11112222") == "**2222"

    def test_short_account(self):
        """Проверка обработки слишком короткого номера"""
        assert mask_account("123") is None

    def test_non_digit_account(self):
        """Проверка обработки нечисловых символов"""
        assert mask_account("abcd5678") is None

    def test_empty_account(self):
        """Проверка обработки пустой строки"""
        assert mask_account("") is None
