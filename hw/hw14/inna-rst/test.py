import unittest
import functions as f
import functions_with_errors as fe

class TestStringMethods(unittest.TestCase):
    def test_greeting_by_name(self):
        result = f.greeting_by_name("Peter")
        self.assertEqual(result, 'Hello Peter!')

    def test_greeting_by_name_empty_string(self):
        result = f.greeting_by_name("")
        self.assertEqual(result, "Hello !")

    def test_greeting_by_name_special_chars(self):
        result = f.greeting_by_name("Nikola")
        self.assertEqual(result, "Hello Nikola!")

        result = f.greeting_by_name("John123")
        self.assertEqual(result, "Hello John123!")

    def test_get_symbol_position(self):
        result = f.get_symbol_position("Hello world!", "o")
        self.assertEqual(result, 5)

        result = f.get_symbol_position("python", "p")
        self.assertEqual(result, 1)

    def test_get_symbol_position_not_found(self):
        result = f.get_symbol_position("hello", "z")
        self.assertEqual(result, "Not found")

    def test_get_symbol_position_multiple_chars_error(self):
        result = f.get_symbol_position("hello", "el")
        self.assertEqual(result, "Error! Symbol can be string with only one letter")

    def test_get_symbol_position_empty_text(self):
        result = f.get_symbol_position("", "a")
        self.assertEqual(result, "Not found")

    def test_get_symbol_position_empty_symbol(self):
        result = f.get_symbol_position("hello", "")
        self.assertEqual(result, 1)

    def test_merge_basic(self):
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3, "d": 4}
        result = f.merge(dict1, dict2)
        expected = {"a": 1, "b": 2, "c": 3, "d": 4}
        self.assertEqual(result, expected)

    def test_merge_overlapping_keys(self):
        dict1 = {"a": 1, "b": 2}
        dict2 = {"b": 3, "c": 4}
        result = f.merge(dict1, dict2)
        expected = {"a": 1, "b": 3, "c": 4}
        self.assertEqual(result, expected)

    def test_merge_original_unchanged(self):
        dict1_original = {"a": 1, "b": 2}
        dict2_original = {"c": 3, "d": 4}
        dict1_copy = dict1_original.copy()
        dict2_copy = dict2_original.copy()

        result = f.merge(dict1_original, dict2_original)

        self.assertEqual(dict1_original, dict1_copy)
        self.assertEqual(dict2_original, dict2_copy)

        expected = {"a": 1, "b": 2, "c": 3, "d": 4}
        self.assertEqual(result, expected)

    def test_merge_empty_dicts(self):
        result = f.merge({}, {})
        self.assertEqual(result, {})

        result = f.merge({"a": 1}, {})
        self.assertEqual(result, {"a": 1})

        result = f.merge({}, {"a": 1})
        self.assertEqual(result, {"a": 1})


class TestFunctionsWithErrors(unittest.TestCase):

    def test_greeting_by_name_with_errors(self):
        result = fe.greeting_by_name("Alice")
        self.assertEqual(result, "Hello name!")

        with self.assertRaises(AssertionError):
            self.assertEqual(result, "Hello Alice!")

    def test_get_symbol_position_with_errors(self):
        result = fe.get_symbol_position("hello", "e")
        self.assertEqual(result, 1)

        result = fe.get_symbol_position("hello", "el")
        self.assertEqual(result, 1)

        result = fe.get_symbol_position("hello", "z")
        self.assertEqual(result, -1)

    def test_merge_with_errors(self):
        dict1_original = {"a": 1, "b": 2}
        dict2_original = {"c": 3, "d": 4}
        dict1_copy = dict1_original.copy()

        result = fe.merge(dict1_original, dict2_original)

        self.assertEqual(dict1_original, {"a": 1, "b": 2, "c": 3, "d": 4})
        self.assertNotEqual(dict1_original, dict1_copy)

        expected = {"a": 1, "b": 2, "c": 3, "d": 4}
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()