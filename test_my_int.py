import unittest

from my_int import MyInt


class TestMyInt(unittest.TestCase):
    def test_0でない整数であること(self):
        with self.assertRaises(ValueError):
            MyInt(0)
            MyInt(1.5)
            MyInt("1")


if __name__ == "__main__":
    unittest.main()
