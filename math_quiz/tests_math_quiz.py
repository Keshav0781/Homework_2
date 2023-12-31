import unittest
from math_quiz import generate_random_integer, generate_arithmetic_operator, calculate_arithmetic_result


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_arithmetic_operator(self):
        # Test if the generated operator is one of '+', '-', or '*'
        valid_operators = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of random values
            operator = generate_arithmetic_operator()
            self.assertIn(operator, valid_operators)

    def test_calculate_arithmetic_result(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '*', '8 * 3', 24),
            (10, 4, '-', '10 - 4', 6),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            result = calculate_arithmetic_result(num1, num2, operator)
            self.assertEqual(result, (expected_problem, expected_answer))


if __name__ == "__main__":
    unittest.main()
