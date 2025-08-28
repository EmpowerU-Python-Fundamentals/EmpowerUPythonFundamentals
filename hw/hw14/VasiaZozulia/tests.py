import unittest

from functions import greeting_by_name, get_symbol_position, merge

from functions_with_errors import greeting_by_name as greeting_by_name_err, get_symbol_position as get_symbol_position_err, merge as merge_err





class TestFunctions(unittest.TestCase):



    def test_greeting_by_name(self):

        self.assertEqual(greeting_by_name("Vasyl"), "Hello Vasyl!")



    def test_greeting_by_name_error(self):

        self.assertEqual(greeting_by_name_err("Vasyl"), "Hello name!")



    def test_get_symbol_position(self):

        self.assertEqual(get_symbol_position("Vasyl", "y"), 4)

        self.assertEqual(get_symbol_position("Vasyl Zozulia", "Z"), 7)

        self.assertEqual(get_symbol_position("Vasyl Zozulia", "p"), "Not found")

        self.assertEqual(get_symbol_position("Vasyl Zozulia", "vz"), "Error! Symbol can be string with only one letter")



    def test_get_symbol_position_error(self):

        self.assertEqual(get_symbol_position_err("Vasyl", "y"), 3)

        self.assertEqual(get_symbol_position_err("Vasyl Zozulia", "Z"), 6)

        self.assertEqual(get_symbol_position_err("Vasyl Zozulia", "p"), -1)

        self.assertEqual(get_symbol_position_err("Vasyl Zozulia", "vz"), -1)



    def test_merge(self):

        dict1 = {"name": "Vasyl", "surname": "zozulia"}

        dict2 = {"surname": "Zozulia", "lang": "python"}

        result = {"name": "Vasyl", "surname": "Zozulia", "lang": "python"}

        self.assertEqual(merge(dict1, dict2), result)



    def test_merge_error(self):

        dict1 = {"country": "Ukraine", "number": 392}

        dict2 = {"number": 28, "month": 8}

        result = {"country": "Ukraine", "number": 28, "month": 8}

        self.assertEqual(merge_err(dict1, dict2), result)





if __name__ == "__main__":

    unittest.main()

