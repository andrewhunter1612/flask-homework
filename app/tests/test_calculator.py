from models.calulator  import Calculator
import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(5, 3)

    def test_add(self):
        self.assertEqual(8, self.alculator.add(self.calculator))