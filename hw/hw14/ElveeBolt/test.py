import unittest
import importlib

from functions import greeting_by_name, get_symbol_position, merge


class TestFunctions(unittest.TestCase):
    def test_greeting_by_name(self):
        self.assertEqual(greeting_by_name("John"), "Hello John!")

    def test_get_symbol_position_incorrect_symbol(self):
        self.assertEqual(
            get_symbol_position("Hello", "ll"),
            "Error! Symbol can be string with only one letter"
        )

    def test_get_symbol_position_success(self):
        self.assertEqual(
            get_symbol_position("Hello", "e"),
            2  # position is 2 because "H e" and counting from 1
        )

    def test_get_symbol_position_not_found(self):
        self.assertEqual(
            get_symbol_position("Hello", "x"),
            "Not found"
        )

    def test_merge_dict1_immutability(self):
        d1 = {"a": 1}
        d2 = {"b": 2}
        result = merge(d1, d2)
        self.assertEqual(d1, {"a": 1})
        self.assertEqual(result, {"a": 1, "b": 2})

    def test_merge_dict2_immutability(self):
        d1 = {"a": 1}
        d2 = {"b": 2}
        result = merge(d1, d2)
        self.assertEqual(d2, {"b": 2})
        self.assertEqual(result, {"a": 1, "b": 2})

    def test_merge_result(self):
        d1 = {"a": 1}
        d2 = {"b": 2}
        result = merge(d1, d2)
        self.assertEqual(result, {"a": 1, "b": 2})



if __name__ == "__main__":
    unittest.main(verbosity=2)
