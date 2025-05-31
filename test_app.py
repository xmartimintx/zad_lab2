import unittest
from app import (
    is_valid_phone_number,
    calculate_triangle_area,
    filter_positive_numbers,
    convert_date_to_iso,
    count_vowels
)

class TestAppFunctions(unittest.TestCase):

    def test_is_valid_phone_number(self):
        self.assertTrue(is_valid_phone_number("+48123456789"))
        self.assertFalse(is_valid_phone_number("123456789"))
        self.assertFalse(is_valid_phone_number("+48abc456789"))

    def test_calculate_triangle_area(self):
        self.assertEqual(calculate_triangle_area(10, 5), 25.0)
        self.assertEqual(calculate_triangle_area(6, 4), 12.0)
        with self.assertRaises(ValueError):
            calculate_triangle_area(-3, 5)

    def test_filter_positive_numbers(self):
        self.assertEqual(filter_positive_numbers([1, -2, 3, 0]), [1, 3])
        self.assertEqual(filter_positive_numbers([-5, -1]), [])
        self.assertEqual(filter_positive_numbers([1.5, 2.3]), [1.5, 2.3])

    def test_convert_date_to_iso(self):
        self.assertEqual(convert_date_to_iso("01-01-2023"), "2023-01-01")
        self.assertEqual(convert_date_to_iso("31-12-1999"), "1999-12-31")
        with self.assertRaises(ValueError):
            convert_date_to_iso("2023/01/01")

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Ala ma kota"), 5)
        self.assertEqual(count_vowels("Król Karol kupił królowej korale"), 14)
        self.assertEqual(count_vowels("123456"), 0)

if __name__ == '__main__':
    unittest.main()