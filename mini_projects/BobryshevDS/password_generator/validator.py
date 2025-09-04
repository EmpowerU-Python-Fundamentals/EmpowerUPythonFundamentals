# validator.py
from typing import Tuple, Optional

def validate_input(length: str, use_letters: bool, use_numbers: bool, use_symbols: bool, use_uppercase: bool) -> Tuple[bool, Optional[str]]:
    """
    Перевіряє вхідні дані для генератора паролів.
    Повертає кортеж: (True, None) у разі успіху або (False, "Повідомлення про помилку") у разі помилки.
    """
    # 1. Перевірка довжини
    try:
        int_length = int(length)
    except ValueError:
        return (False, "Довжина має бути числом.")

    if int_length <= 0:
        return (False, "Довжина пароля має бути більше 0.")

    # 2. Перевірка, чи обрано хоча б один тип символів
    if not any([use_letters, use_numbers, use_symbols, use_uppercase]):
        return (False, "Оберіть хоча б один тип символів (літери, цифри, тощо).")
    
    return (True, None)