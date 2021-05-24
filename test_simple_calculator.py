import unittest
from calculator import SimpleCalculator


class AdditionTestSuite(unittest.TestCase):
    def setUp(self):
        """ Executed before every test case """
        self.calculator = SimpleCalculator()

    def tearDown(self):
        """ Executed after every test case """
        print("\ntearDown executing after the test case. Result:")

    def test_addition_two_numbers(self):
        result = self.calculator.addition(5, 6)
        self.assertEqual(result, 11)

    def test_addition_number_string(self):
        result = self.calculator.addition(5, "6")
        self.assertEqual(result, "ERROR")

    def test_addition_negative_numbers(self):
        result = self.calculator.addition(-5, -6)
        self.assertEqual(result, -11)
        self.assertNotEqual(result, 11)


class DivisionTestSuite(unittest.TestCase):
    def setUp(self):
        """ Executed before every test case """
        self.calculator = SimpleCalculator()

    def test_divide_by_zero_exception(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(10, 0)


class MultiplicationTestSuite(unittest.TestCase):
    def setUp(self):
        """ Executed before every test case """
        self.calculator = SimpleCalculator()

    def tearDown(self):
        """ Executed after every test case """
        print("\ntearDown executing after the test case. Result:")

    def test_multiplication_two_numbers(self):
        result = self.calculator.multiply(5, 6)
        self.assertEqual(result, 30)

    def test_multiplication_number_string(self):
        result = self.calculator.multiply(5, "6")
        self.assertEqual(result, "ERROR")

    def test_multiplication_negative_numbers(self):
        result = self.calculator.multiply(-5, -6)
        self.assertEqual(result, 30)
        self.assertNotEqual(result, -30)


class SubtractionTestSuite(unittest.TestCase):
    def setUp(self):
        """ Executed before every test case """
        self.calculator = SimpleCalculator()

    def tearDown(self):
        """ Executed after every test case """
        print("\ntearDown executing after the test case. Result:")

    def test_subtraction_two_numbers(self):
        result = self.calculator.subtraction(7, 6)
        self.assertEqual(result, 1)

    def test_subtraction_negative_numbers(self):
        result = self.calculator.multiply(-5, -6)
        self.assertEqual(result, 1)

    def test_subtraction_negative_result(self):
        result = self.calculator.multiply(-9, 6)
        self.assertEqual(result, -15)
        self.assertNotEqual(result, 15)


# Execute all the tests when the file is executed
if __name__ == "__main__":
    unittest.main()
