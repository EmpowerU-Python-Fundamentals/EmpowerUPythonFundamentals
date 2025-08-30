import unittest


class BaseTestsMixin:
    funcs = None  

    def test_greeting_by_name(self):
        self.assertEqual(
            self.funcs.greeting_by_name("Illia"), "Hello Illia!"
        )

    def test_get_symbol_position_symbol_incorrect(self):
        self.assertEqual(
            self.funcs.get_symbol_position("abc", "ab"),
            "Error! Symbol can be string with only one letter"
        )

    def test_get_symbol_position_success(self):
        self.assertEqual(
            self.funcs.get_symbol_position("hello", "e"), 2
        )

    def test_get_symbol_position_not_found(self):
        self.assertEqual(
            self.funcs.get_symbol_position("hello", "z"), "Not found"
        )

    def test_merge_result(self):
        d1 = {"a": 1}
        d2 = {"b": 2}
        merged = self.funcs.merge(d1, d2)
        self.assertEqual(merged, {"a": 1, "b": 2})

    def test_merge_dict1_immutability(self):
        d1 = {"a": 1}
        d1_copy = d1.copy()
        d2 = {"b": 2}
        _ = self.funcs.merge(d1, d2)
        self.assertEqual(d1, d1_copy)

    def test_merge_dict2_immutability(self):
        d1 = {"a": 1}
        d2 = {"b": 2}
        d2_copy = d2.copy()
        _ = self.funcs.merge(d1, d2)
        self.assertEqual(d2, d2_copy)


class TestFunctions(BaseTestsMixin, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import functions as funcs
        cls.funcs = funcs


class TestFunctionsWithErrors(BaseTestsMixin, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import functions_with_errors as funcs
        cls.funcs = funcs


if __name__ == "__main__":
    unittest.main(verbosity=2)
# =================================================