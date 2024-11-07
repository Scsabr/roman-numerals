import unittest
from converter import roman_to_decimal

# test script kindly provided by chatGPT

class TestRomanToDecimalConverter(unittest.TestCase):
    
    def test_single_numerals(self):
        self.assertEqual(roman_to_decimal('I'), 1)
        self.assertEqual(roman_to_decimal('V'), 5)
        self.assertEqual(roman_to_decimal('X'), 10)
        self.assertEqual(roman_to_decimal('L'), 50)
        self.assertEqual(roman_to_decimal('C'), 100)
        self.assertEqual(roman_to_decimal('D'), 500)
        self.assertEqual(roman_to_decimal('M'), 1000)

    def test_basic_combinations(self):
        self.assertEqual(roman_to_decimal('II'), 2)
        self.assertEqual(roman_to_decimal('III'), 3)
        self.assertEqual(roman_to_decimal('VI'), 6)
        self.assertEqual(roman_to_decimal('XV'), 15)
        self.assertEqual(roman_to_decimal('LX'), 60)

    def test_subtractive_notation(self):
        self.assertEqual(roman_to_decimal('IV'), 4)
        self.assertEqual(roman_to_decimal('IX'), 9)
        self.assertEqual(roman_to_decimal('XL'), 40)
        self.assertEqual(roman_to_decimal('XC'), 90)
        self.assertEqual(roman_to_decimal('CD'), 400)
        self.assertEqual(roman_to_decimal('CM'), 900)

    def test_complex_numerals(self):
        self.assertEqual(roman_to_decimal('XIV'), 14)
        self.assertEqual(roman_to_decimal('XXIX'), 29)
        self.assertEqual(roman_to_decimal('XLII'), 42)
        self.assertEqual(roman_to_decimal('XCIX'), 99)
        self.assertEqual(roman_to_decimal('DCLXVI'), 666)
        self.assertEqual(roman_to_decimal('MCMXCIV'), 1994)
        self.assertEqual(roman_to_decimal('MMXXIII'), 2023)

    def test_invalid_numerals(self):
        with self.assertRaises(ValueError):
            roman_to_decimal('IIII')  # Invalid repetition
        with self.assertRaises(ValueError):
            roman_to_decimal('VV')    # Invalid repetition
        with self.assertRaises(ValueError):
            roman_to_decimal('IC')    # Invalid subtractive combination
        with self.assertRaises(ValueError):
            roman_to_decimal('MMMM')  # Invalid numeral beyond usual limits

if __name__ == '__main__':
    unittest.main(verbosity=3)
