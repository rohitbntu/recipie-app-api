from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that 2 numbers are addded together"""
        self.assertEqual(add(3,8),11)

    def test_subtract_numbers(self):
        """Test that 2 numbers are addded together"""
        self.assertEqual(subtract(3,8),5)
