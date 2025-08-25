import unittest
# from functions import greeting_by_name, get_symbol_position, merge
from functions_with_errors import greeting_by_name, get_symbol_position, merge

class GreetingByNameTests(unittest.TestCase):
    def  test_greeting_by_name(self):
        self.assertEqual(greeting_by_name("Yulia"), "Hello Yulia!")
        self.assertEqual(greeting_by_name("Anna"), "Hello Anna!")
        self.assertEqual(greeting_by_name(""), "Hello !")


class GetSymbolPosition(unittest.TestCase):
    def test_found_symbol(self):
        self.assertEqual(get_symbol_position("hello", "e"), 2)

    def test_not_found_symbol(self):
        self.assertEqual(get_symbol_position("hello", "z"), "Not found")

    def test_symbol_incorrect(self):
        self.assertEqual(
            get_symbol_position("hello", "ll"),
            "Error! Symbol can be string with only one letter"
        )
        
class MergeTests(unittest.TestCase):
    def test_merge_disjoint_dicts(self):
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3, "d": 4}
        result = merge(dict1, dict2)
        self.assertEqual(result, {"a": 1, "b": 2, "c": 3, "d": 4})

    def test_merge_with_overwrite(self):
        dict1 = {"a":1, "b":2}
        dict2 = {"b": 20, "c":3}
        result = merge(dict1, dict2)
        self.assertEqual(result, {"a":1, "b":20, "c":3})

    def test_merge_empty_dict(self):
        dict1 = {"a": 1, "b":2}
        dict2 = {}
        result = merge(dict1, dict2)
        self.assertEqual(result, {"a":1, "b":2})

    def test_merge_is_immutable(self):
        dict1 = {"a": 1}
        dict2 = {"b": 2}
        result = merge(dict1, dict2)
        self.assertEqual(dict1, {"a": 1})
        self.assertEqual(dict2, {"b": 2})
        self.assertEqual(result, {"a": 1, "b": 2})



if __name__ == "__main__":
    unittest.main()
       