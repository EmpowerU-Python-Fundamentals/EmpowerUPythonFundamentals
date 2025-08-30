import unittest as ut

### Comment / unkomment appropriate line below
# import functions as testable
import functions_with_errors as testable

class greeting_by_name_tests(ut.TestCase):
    def test_greeting_by_name__should_process_lowercase_name(self):
        result = testable.greeting_by_name("somename")
        self.assertEqual(
            result,
            "Hello somename!",
            "Wrong result."
        )

    def test_greeting_by_name__should_process_regular_name(self):
        result = testable.greeting_by_name("Somename")
        self.assertEqual(
            result,
            "Hello Somename!",
            "Wrong result."
        )

    def test_greeting_by_name__should_process_empty_name(self):
        result = testable.greeting_by_name("")
        self.assertEqual(
            result,
            "Hello !",
            "Wrong result."
        )


class get_symbol_position_tests(ut.TestCase):
    def test_get_symbol_position__should_return_error(self):
        result = testable.get_symbol_position("Some Text", "s ")
        expected = "Error! Symbol can be string with only one letter"
        self.assertEqual(result, expected, 
                         "Should return the error when symbol is too long.")
    
    def test_get_symbol_position__should_return_Not_found(self):
        result = testable.get_symbol_position("Some Text", "-")
        expected = "Not found"
        self.assertEqual(result, expected, 
                         "Should return 'Not found' when symbol is not found.")
    
    def test_get_symbol_position__should_return_first_occurence_position(self):
        result = testable.get_symbol_position("Some Text", "e")
        expected = 4
        self.assertEqual(result, expected, 
                         "Should return 1-based position of the first ocurrence.")
    
    def test_get_symbol_position__should_return_1(self):
        result = testable.get_symbol_position("Some Text", "")
        expected = 1
        self.assertEqual(result, expected, 
                         "Should return 1 when symbol is empty.")


class merge_tests(ut.TestCase):
    def setUp(self):
        self.dict1 = {"a": "aaa", "b": "bbb", "c": "ccc"}
        self.dict2 = {"a": "aaa+", "d": "ddd", "e": "eee"}
        self.expected = {"a": "aaa+", "b": "bbb", "c": "ccc", "d": "ddd", "e": "eee"}

    def test_merge__should_merge_dictionaries(self):
        result = testable.merge(self.dict1, self.dict2)
        self.assertDictEqual(result, self.expected, 
                             "Shold return merged dictionary.")

    def test_merge__should_return_new_dictionary(self):
        result = testable.merge(self.dict1, self.dict2)
        self.assertNotEqual(result, self.dict1, 
                             "Shold return new dictionary.")
        self.assertNotEqual(result, self.dict2, 
                             "Shold return new dictionary.")

    def test_merge__should_not_change_source_dictionaries(self):
        dict1_copy = self.dict1.copy()
        dict2_copy = self.dict2.copy()
        testable.merge(self.dict1, self.dict2)
        self.assertDictEqual(self.dict1, dict1_copy,
                             "Should not change the first dictionary.")
        self.assertDictEqual(self.dict2, dict2_copy,
                             "Should not change the second dictionary.")

if __name__ == "__main__":
    ut.main()