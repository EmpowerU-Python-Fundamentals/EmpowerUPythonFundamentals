import unittest
import functions
import functions_with_errors

class TestFunctions(unittest.TestCase):

    # Тестування greeting_by_name
    def test_greeting_by_name_valid(self):
        self.assertEqual(functions.greeting_by_name("Nastia"), "Hello, Nastia!")
        self.assertEqual(functions_with_errors.greeting_by_name("Nastia"), "Hello, Nastia!")

    def test_greeting_by_name_empty(self):
        self.assertEqual(functions.greeting_by_name(""), "Hello, !")
        with self.assertRaises(ValueError):
            functions_with_errors.greeting_by_name("")

    def test_greeting_by_name_none(self):
        with self.assertRaises(TypeError):
            functions.greeting_by_name(None)
        with self.assertRaises(TypeError):
            functions_with_errors.greeting_by_name(None)

    # Тестування get_symbol_position
    def test_get_symbol_position_success(self):
        self.assertEqual(functions.get_symbol_position("hello", "l"), 2)
        with self.assertRaises(ValueError):
            functions_with_errors.get_symbol_position("hello", "l")

    def test_get_symbol_position_incorrect_symbol(self):
        with self.assertRaises(TypeError):
            functions.get_symbol_position("hello", None)
        with self.assertRaises(TypeError):
            functions_with_errors.get_symbol_position("hello", None)

    def test_get_symbol_position_not_found(self):
        self.assertEqual(functions.get_symbol_position("hello", "z"), -1)
        with self.assertRaises(ValueError):
            functions_with_errors.get_symbol_position("hello", "z")

    # Тестування для merge
    def test_merge_success(self):
        dict1 = {"a": 1}
        dict2 = {"b": 2}
        expected = {"a": 1, "b": 2}
        self.assertEqual(functions.merge(dict1, dict2), expected)
        self.assertEqual(functions_with_errors.merge(dict1, dict2), expected)

    def test_merge_dict1_immutability(self):
        dict1 = {"a": 1}
        dict2 = {"b": 2}
        original_dict1 = dict1.copy()
        functions.merge(dict1, dict2)
        self.assertEqual(dict1, original_dict1)
        dict1_error = {"a": 1}
        functions_with_errors.merge(dict1_error, dict2)
        self.assertNotEqual(dict1_error, original_dict1)

    def test_merge_dict2_immutability(self):
        dict1 = {"a": 1}
        dict2 = {"b": 2}
        original_dict2 = dict2.copy()
        functions.merge(dict1, dict2)
        self.assertEqual(dict2, original_dict2)
        functions_with_errors.merge(dict1, dict2)
        self.assertEqual(dict2, original_dict2)

if __name__ == '__main__':
    unittest.main()