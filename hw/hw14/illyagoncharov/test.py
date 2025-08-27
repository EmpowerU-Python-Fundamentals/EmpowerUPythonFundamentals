import unittest
from functions import greeting_by_name,get_symbol_position,merge

msg1 = "Test get_symbol_position(text, symbol)"
msg2 = 'Test merge(dict1,dict2)'
class Tests(unittest.TestCase):
    msg = "Test get_symbol_position(text, symbol)"
    def test_greeting_by_name(self):
        res = greeting_by_name("Ihor")
        self.assertEqual(greeting_by_name("Ihor"), "Hello Ihor!", 'Test greeting_by_name(name) is Falied')

    def test_get_symbol_position_incorrect(self):
        self.assertEqual(get_symbol_position("abcdef","nm"),
                         "Error! Symbol can be string with only one letter",
                         f"{msg1} when symbol is incorrect is Failed")

    def test_get_symbol_position(self):
            self.assertEqual(get_symbol_position("abcdef", "a"),
                    1,
                    f"{msg1} message with success is Failed")

    def test_get_symbol_position_notfound(self):
        self.assertEqual(get_symbol_position("abcdef", "t"),
                         "Not found",
                         f"{msg1} when symbol was not found is Failed")

    def test_merge_check_dict1(self):
        dict1 = {"1": "a", "2": "b"}
        dict2 = {"3": "c", "4": "d"}
        s = merge(dict1,dict2)
        self.assertNotEqual(id(s),
                             id(dict1), f"{msg2} dict1 immutability is Failed")

    def test_merge_check_dict2(self):
        dict1 = {"1": "a", "2": "b"}
        dict2 = {"3": "c", "4": "d"}
        s = merge(dict1, dict2)
        s['3'] = "abc"
        self.assertEqual(s['3'], dict2['3'], f"{msg2} dict2 immutability is Passed")



    def test_merge(self):
        dict1 = {"1": "a", "2": "b"}
        dict2 = {"3": "c", "4": "d"}
        s = merge(dict1, dict2)
        self.assertNotEqual(merge(dict1 = dict1, dict2=dict2),
                         {'1': 'a', '2': 'b', '3': 'c', '4': 'd'}, f"{msg2} is Passed")


if __name__ == "__main__":
    unittest.main()