import unittest

from code.fibonacci import Fibonacci


class test_fibonacci(unittest.TestCase):
    def setUp(self):
        self.fibonacci = Fibonacci()


    def test_should_fibonacci_number_of_months_1_and_pairs_produced_3_return_1(self):
        self.assertEqual(1, self.fibonacci.compute(1,3))

    def test_should_fibonacci_number_of_months_2_and_pairs_produced_3_return_1(self):
        self.assertEqual(1, self.fibonacci.compute(2,3))

    def test_should_fibonacci_number_of_months_3_and_pairs_produced_3_return_4(self):
        self.assertEqual(4, self.fibonacci.compute(3,3))

    def test_should_fibonacci_number_of_months_4_and_pairs_produced_3_return_7(self):
        self.assertEqual(7, self.fibonacci.compute(4,3))

    def test_should_fibonacci_number_of_months_5_and_pairs_produced_3_return_19(self):
        self.assertEqual(19, self.fibonacci.compute(5,3))

    def test_should_fibonacci_number_of_months_6_and_pairs_produced_3_return_40(self):
        self.assertEqual(40, self.fibonacci.compute(6,3))

    def test_should_fibonacci_number_of_months_7_and_pairs_produced_3_return_97(self):
        self.assertEqual(97, self.fibonacci.compute(7,3))

if __name__ == '__main__':
    unittest.main()

