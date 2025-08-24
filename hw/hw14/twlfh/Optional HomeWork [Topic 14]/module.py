import unittest
from functions import *
# from functions_with_errors import *

class TestFunc(unittest.TestCase):
    def test_greeting_by_name(self):
        self.assertEqual(greeting_by_name('Vlad'), 'Hello Vlad!')

    def test_symbol_position(self):
        self.assertEqual(get_symbol_position('hello', 'h'), 1)

    def test_symbol_negative_position(self):
        self.assertEqual(get_symbol_position('hello', 'h'), 1)

    def test_symbol_position_out_of_range(self):
        self.assertEqual(get_symbol_position('hello', 'hh'),
                         "Error! Symbol can be string with only one letter")

    def test_symbol_position_not_found(self):
        self.assertEqual(get_symbol_position('hello', 'x'), "Not found")

    def test_merge(self):
        self.assertEqual(merge({1: 'a', 2: 'b'}, {3: 'c', 4: 'd'}),
                         {1: 'a', 2: 'b', 3: 'c', 4: 'd'})

    def test_merge_empty_first_dict(self):
        self.assertEqual({},{1: 'f', 2: 'c'}, {1: 'f', 2: 'c'} )

    def test_merge_empty_second_dict(self):
        self.assertEqual({1: 'f', 2: 'c'},{}, {1: 'f', 2: 'c'} )










if __name__ == '__main__':
    unittest.main()


