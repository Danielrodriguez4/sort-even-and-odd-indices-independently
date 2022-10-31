import unittest
from solution_2164 import Solution


class Test791(unittest.TestCase):

    def setUp(self):
        self.function = Solution()

    def test_1(self):
        resultado = self.function.sortEvenOdd([4, 1, 2, 3])
        self.assertEqual(resultado, [2, 3, 4, 1])

    def test_2(self):
        resultado = self.function.sortEvenOdd([8, 7, 1, 9])
        self.assertEqual(resultado, [1, 9, 8, 7])


if __name__ == '__main__':
    unittest.main()
