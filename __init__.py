import unittest


class ProblemTests(unittest.TestCase):
    def test_problem_1(self):
        from p001 import func
        self.assertEqual(func(10), 23)
        self.assertEqual(func(1000), 233168)

    def test_problem_2(self):
        from p002 import func
        self.assertEqual(func(4000000), 4613732)

    def test_problem_3(self):
        from p003 import is_prime, func
        self.assertEqual(is_prime(0), False)
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(5), True)
        self.assertEqual(is_prime(15), False)
        self.assertEqual(is_prime(17), True)
        self.assertEqual(func(14), 7)
        self.assertEqual(func(13195), 29)
        self.assertEqual(func(600851475143), 6857)

    def test_problem_15(self):
        from p015 import factorial, func
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(func(0), 0)
        self.assertEqual(func(1), 2)
        self.assertEqual(func(2), 6)
        self.assertEqual(func(20), 137846528820)

if __name__ == '__main__':
    unittest.main()
