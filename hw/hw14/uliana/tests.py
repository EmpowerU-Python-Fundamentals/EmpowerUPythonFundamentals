import unittest
import functions
import functions_with_errors


class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.modules = [functions, functions_with_errors]

    def test_greeting(self):
        for module in self.modules:
            with self.subTest(module=module.__name__):
                self.assertEqual(module.greeting_by_name("Sergii"), "Hello Sergii!")

    def test_get_pos(self):
        for module in self.modules:
            with self.subTest(module=module.__name__):
                self.assertEqual(module.get_symbol_position("hello", "el"), "Error! Symbol can be string with only one letter")
                self.assertEqual(module.get_symbol_position(123, "e"), "Error! The text is not a string.")
                self.assertEqual(module.get_symbol_position("hello", "e"), "2")
                self.assertEqual(module.get_symbol_position("hello", "o"), "Not found")
                self.assertEqual(module.get_symbol_position("hello", ""), "Empty symbol")

    def test_merge(self):
        for module in self.modules:
            with self.subTest(module=module.__name__):
                d1 = {"a": 1}
                d2 = {"b": 2}
                result = module.merge(d1, d2)
                self.assertEqual(result, {"a": 1, "b": 2})
                self.assertEqual(d1, {"a": 1})
                self.assertEqual(d2, {"b": 2})

if __name__ == "__main__":
    unittest.main()