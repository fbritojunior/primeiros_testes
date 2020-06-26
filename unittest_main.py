from main import *
import unittest


class TestSoma(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(soma(3,3), 6, "Should be 6")


if __name__ == '__main__':
    unittest.main()
