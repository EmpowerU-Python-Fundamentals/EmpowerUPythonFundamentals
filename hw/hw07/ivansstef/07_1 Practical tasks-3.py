def count_characters(s):
    """    Повертає словник з кількістю входжень кожного символу в рядку."""
    result = {}
    for char in s:
        result[char] = result.get(char, 0) + 1
    return result

# Приклад використання
print(count_characters("hello"))  # ➤ {'h': 1, 'e': 1, 'l': 2, 'o': 1}
