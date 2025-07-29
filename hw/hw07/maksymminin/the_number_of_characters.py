def count_characters(text):
    """Рахує, скільки разів кожна літера зустрічається у тексті."""
    result = {}
    for letter in text:
        if letter in result:
            result[letter] = result[letter] + 1
        else:
            result[letter] = 1
    return result

# Запит до користувача
user_input = input("Введіть слово або текст: ")

# Вивід результату
print("Кількість символів:", count_characters(user_input))