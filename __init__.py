import unittest


class ProblemTests(unittest.TestCase):
    def test_problem_1(self):
        from problem_1 import func
        self.assertEqual(func(10), 23)
        self.assertEqual(func(1000), 233168)


if __name__ == '__main__':
    unittest.main()
