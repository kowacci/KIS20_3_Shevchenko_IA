from main import replace_symbols
import unittest

class TestReplaceSymbols(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(replace_symbols(''), '')
    def test_abc(self):
        self.assertEqual(replace_symbols('abc'), 'abc')

    def test_ab(self):
        self.assertEqual(replace_symbols('a*!&?-_b(){}[]'), 'ab')

if __name__ == '__main__':
    unittest.main()

