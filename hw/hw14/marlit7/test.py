import unittest
import functions
import functions_with_errors


class TestFunctions(unittest.TestCase):

    def test_greeting_by_name(self):
        # correct data
        self.assertEqual(functions.greeting_by_name("John"), "Hello John!")
        # incorrect data
        self.assertEqual(functions_with_errors.greeting_by_name("John"), "Hello name!")

    def test_get_symbol_position(self):
        # correct
        self.assertEqual(functions.get_symbol_position("hello", "e"), 2)  # find
        self.assertEqual(functions.get_symbol_position("hello", "a"), "Not found")  # not found
        self.assertEqual(functions.get_symbol_position("hello", "he"),
                         "Error! Symbol can be string with only one letter")  # error

        # incorrect
        self.assertEqual(functions_with_errors.get_symbol_position("hello", "e"), 1)
        self.assertEqual(functions_with_errors.get_symbol_position("hello", "a"), -1)
        self.assertEqual(functions_with_errors.get_symbol_position("hello", "he"), 0)

    def test_merge(self):
        dict1 = {"a": 1}
        dict2 = {"b": 2}

        result = functions.merge(dict1, dict2)
        self.assertEqual(result, {"a": 1, "b": 2})
        self.assertEqual(dict1, {"a": 1})

        result_err = functions_with_errors.merge(dict1, dict2)
        self.assertEqual(result_err, {"a": 1, "b": 2})
        self.assertEqual(dict1, {"a": 1, "b": 2})


if __name__ == "__main__":
    unittest.main()