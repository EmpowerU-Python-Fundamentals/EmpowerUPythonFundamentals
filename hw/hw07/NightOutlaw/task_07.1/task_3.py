def count_characters(text) -> dict:
    """This function calculates the number of characters included in given string"""
    result = {}
    for char in text.lower():                       # Приводимо до нижнього регістру для уніфікації
        if char.isalpha() or char.isnumeric():      # Відфільтровуємо всі символи окрім літер та цифр
            result[char] = result.get(char, 0) + 1  # Обчислюємо кількість для кожного відфільтрованого символа
    return result
