import unittest
from math_quiz import generate_random_integer, random_arithmetic_operation, arithmetic_operation


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_arithmetic_operation(self):
        """ Test if the function returns a valid arithmetic operation """
        valid_operators = ['+', '-', '*']
        
        for _ in range(1000):  # Test with a large number multiple times for randomness
            operator = get_random_operator()
            self.assertIn(operator, valid_operators)
        

    def test_arithmetic_operation(self):
            """Test if the function can correctly create math problems and compute the answers."""
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '-', '8 - 3', 5),
            (4, 6, '*', '4 * 6', 24),
            (1, 1, '+', '1 + 1', 2),
            (6, 2, '*', '6 * 2', 12)
            
            ]

            for number1, number2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = arithmetic_operation(number1, number2, operation)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)
                

if __name__ == "__main__":
    unittest.main()
