from main import replace_symbols
import unittest

class TestReplaceSymbols(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(replace_symbols(''), '')

if __name__ == '__main__':
    unittest.main()