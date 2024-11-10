import unittest
from math_quiz import generate_random_integer, generate_random_operator, create_math_problem


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        """
        Test that random integers generated are within the specified range.
        """
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Check a large sample size
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, "Generated number is out of range.")

    def test_generate_random_operator(self):
        """
        Test that the generated operator is one of the expected operators.
        """
        operators = {'+', '-', '*'}
        for _ in range(1000):  # Check a large sample size
            op = generate_random_operator()
            self.assertIn(op, operators, "Generated operator is not one of '+', '-', '*'.")

    def test_create_math_problem(self):
        """
        Test that create_math_problem correctly generates the math problem statement and answer.
        """
        test_cases = [
            # Valid cases for each operator
            (5, 2, '+', '5 + 2', 7),
            (10, 4, '-', '10 - 4', 6),
            (3, 3, '*', '3 * 3', 9),
            
            # Edge cases with zero
            (0, 7, '+', '0 + 7', 7),
            (9, 0, '-', '9 - 0', 9),
            (0, 0, '*', '0 * 0', 0),

            # Negative numbers
            (-3, 5, '+', '-3 + 5', 2),
            (8, -2, '-', '8 - -2', 10),
            (-2, -3, '*', '-2 * -3', 6),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            with self.subTest(num1=num1, num2=num2, operator=operator):
                # Manually set the operator in create_math_problem
                problem, answer = create_math_problem(num1, num2, operator)
                self.assertEqual(problem, expected_problem, f"Expected problem statement '{expected_problem}', but got '{problem}'.")
                self.assertEqual(answer, expected_answer, f"Expected answer {expected_answer}, but got {answer}.")


if __name__ == "__main__":
    unittest.main()
