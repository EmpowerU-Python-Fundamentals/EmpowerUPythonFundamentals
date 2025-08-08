def count_characters(text):
    """
    Обчислює кількість кожного символу у вхідному рядку.

    Аргументи:
    text (str): рядок, у якому потрібно порахувати символи

    Повертає:
    dict: словник, де ключі — символи, а значення — кількість їх появ
    """
    result = {}
    for char in text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result
