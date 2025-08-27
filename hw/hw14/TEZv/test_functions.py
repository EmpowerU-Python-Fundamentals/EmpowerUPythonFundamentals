import unittest
import functions as correct_functions
import functions_with_errors as error_functions

# A list of modules to test
MODULES_TO_TEST = [
    (correct_functions, "Correct Functions"),
    (error_functions, "Functions with Errors")
]

class TestFunctions(unittest.TestCase):
    """
    This class contains unit tests for the functions in both modules.
    It's designed to be reusable for testing both correct and incorrect versions.
    """

    def test_greeting_by_name(self):
        """
        Test the greeting_by_name function.
        - Correct function: should return "Hello {name}!".
        - Error function: should return "Hello name!".
        """
        for module, module_name in MODULES_TO_TEST:
            with self.subTest(module=module_name):
                # Test with a simple name
                self.assertEqual(module.greeting_by_name("Alex"), f"Hello Alex!",
                                 f"Test failed for {module_name} with name 'Alex'.")

    def test_get_symbol_position(self):
        """
        Test the get_symbol_position function with different cases.
        - Symbol found
        - Symbol not found
        - Incorrect symbol (more than one character)
        """
        for module, module_name in MODULES_TO_TEST:
            with self.subTest(module=module_name):
                # Test when the symbol is found
                self.assertEqual(module.get_symbol_position("Hello World", "W"), 7,
                                 f"Test failed for {module_name} when symbol is found.")
                
                # Test when the symbol is not found
                self.assertEqual(module.get_symbol_position("Hello World", "z"), "Not found",
                                 f"Test failed for {module_name} when symbol is not found.")
                
                # Test when the symbol is incorrect (more than one character)
                self.assertEqual(module.get_symbol_position("Hello World", "or"), 
                                 "Error! Symbol can be string with only one letter",
                                 f"Test failed for {module_name} with incorrect symbol.")
                
    def test_merge(self):
        """
        Test the merge function.
        - Correct function: should return a new merged dictionary and not modify original dicts.
        - Error function: should modify the first dictionary in place.
        """
        for module, module_name in MODULES_TO_TEST:
            with self.subTest(module=module_name):
                dict1 = {"a": 1, "b": 2}
                dict2 = {"c": 3, "d": 4}
                expected_result = {"a": 1, "b": 2, "c": 3, "d": 4}
                
                # Test the merged result
                self.assertEqual(module.merge(dict1, dict2), expected_result,
                                 f"Test failed for {module_name} on merge result.")
                
                # Test immutability of the first dictionary
                # The correct function creates a new dictionary, so dict1 should be unchanged.
                # The error function modifies dict1 in place, so the test will fail for it.
                if module_name == "Correct Functions":
                    self.assertEqual(dict1, {"a": 1, "b": 2}, 
                                     f"Test failed for {module_name}: dict1 was mutated.")
                else:
                    self.assertNotEqual(dict1, {"a": 1, "b": 2}, 
                                        f"Test failed for {module_name}: dict1 was not mutated as expected.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

