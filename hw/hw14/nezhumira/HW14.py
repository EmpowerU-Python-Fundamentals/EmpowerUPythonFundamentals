import unittest
import functions
import functions_with_errors


class TestFunctions(unittest.TestCase):

    # ---------- greeting_by_name ----------
    def test_greeting_by_name(self):
        # Correct function
        self.assertEqual(functions.greeting_by_name("Alice"), "Hello Alice!")
        # Erroneous function
        self.assertNotEqual(functions_with_errors.greeting_by_name("Alice"), "Hello Alice!")
        self.assertEqual(functions_with_errors.greeting_by_name("Alice"), "Hello name!")

    # ---------- get_symbol_position ----------
    def test_get_symbol_position_success(self):
        self.assertEqual(functions.get_symbol_position("hello", "e"), 2)
        self.assertEqual(functions_with_errors.get_symbol_position("hello", "e"), 1)  # find() returns 1

    def test_get_symbol_position_not_found(self):
        self.assertEqual(functions.get_symbol_position("hello", "z"), "Not found")
        self.assertEqual(functions_with_errors.get_symbol_position("hello", "z"), -1)

    def test_get_symbol_position_incorrect_symbol(self):
        self.assertEqual(
            functions.get_symbol_position("hello", "ab"),
            "Error! Symbol can be string with only one letter"
        )
        # Wrong behavior: should error, but returns .find() position (-1)
        self.assertEqual(functions_with_errors.get_symbol_position("hello", "ab"), -1)

    # ---------- merge ----------
    def test_merge_dicts(self):
        d1 = {"a": 1}
        d2 = {"b": 2}
        result_correct = functions.merge(d1, d2)
        result_error = functions_with_errors.merge(d1.copy(), d2)

        # Correct result must contain both
        self.assertEqual(result_correct, {"a": 1, "b": 2})
        # Erroneous result also contains both
        self.assertEqual(result_error, {"a": 1, "b": 2})

    def test_merge_immutability_dict1(self):
        d1 = {"a": 1}
        d2 = {"b": 2}
        _ = functions.merge(d1, d2)
        self.assertEqual(d1, {"a": 1})  # dict1 unchanged

        _ = functions_with_errors.merge(d1, d2)
        self.assertEqual(d1, {"a": 1, "b": 2})  # dict1 modified (bug)

    def test_merge_immutability_dict2(self):
        d1 = {"a": 1}
        d2 = {"b": 2}
        _ = functions.merge(d1, d2)
        self.assertEqual(d2, {"b": 2})  # dict2 unchanged

        _ = functions_with_errors.merge(d1, d2)
        self.assertEqual(d2, {"b": 2})  # still unchanged (same as correct)


if __name__ == "__main__":
    unittest.main()
