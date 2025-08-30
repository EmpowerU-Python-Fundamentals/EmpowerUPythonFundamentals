import unittest
# Використання псевдонімів для імпортованих модулів
import functions as f
import functions_with_errors as fe

class TestFunctions(unittest.TestCase):
    """
    Тести для правильних функцій з файлу functions.py
    """

    def test_greeting_by_name(self):
        # Перевірка коректного привітання з іменем
        self.assertEqual(f.greeting_by_name("John"), "Hello John!")

    def test_get_symbol_position_found(self):
        # Тест для випадку, коли символ знайдено
        self.assertEqual(f.get_symbol_position("Hello", "l"), 3)

    def test_get_symbol_position_not_found(self):
        # Тест для випадку, коли символ не знайдено
        self.assertEqual(f.get_symbol_position("Hello", "z"), "Not found")

    def test_get_symbol_position_error(self):
        # Тест для випадку, коли символ має більше одного символу
        self.assertEqual(f.get_symbol_position("Hello", "ll"), "Error! Symbol can be string with only one letter")

    def test_merge(self):
        # Тест для коректного злиття словників
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3, "d": 4}
        merged_dict = f.merge(dict1, dict2)
        self.assertDictEqual(merged_dict, {"a": 1, "b": 2, "c": 3, "d": 4})
        # Перевірка, що оригінальні словники залишились незмінними
        self.assertDictEqual(dict1, {"a": 1, "b": 2})
        self.assertDictEqual(dict2, {"c": 3, "d": 4})

# ---
# Тести для функцій з помилками
# ---

class TestFunctionsWithErrors(unittest.TestCase):
    """
    Тести для функцій з помилками з файлу functions_with_errors.py
    """

    def test_greeting_by_name_error(self):
        # Цей тест ВПАДЕ, оскільки функція повертає "Hello name!"
        self.assertEqual(fe.greeting_by_name("John"), "Hello John!")

    def test_get_symbol_position_error_found(self):
        # Цей тест ВПАДЕ, оскільки функція повертає 0-індексовану позицію (2), а не 1-індексовану (3)
        self.assertEqual(fe.get_symbol_position("Hello", "l"), 3)
    
    def test_get_symbol_position_error_not_found(self):
        # Цей тест ВПАДЕ, оскільки функція повертає -1, а не "Not found"
        self.assertEqual(fe.get_symbol_position("Hello", "z"), "Not found")
    
    def test_merge_error(self):
        # Цей тест ВПАДЕ, оскільки функція змінює оригінальний словник (dict1)
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3, "d": 4}
        # Виконуємо злиття. Результат буде правильним.
        fe.merge(dict1, dict2)
        # Асерт, який перевіряє, що оригінальний словник не змінився. Він ВПАДЕ.
        self.assertDictEqual(dict1, {"a": 1, "b": 2})