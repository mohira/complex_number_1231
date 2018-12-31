import unittest

from my_int import MyInt


class TestMyInt(unittest.TestCase):
    def test_0でない整数であること(self):
        with self.assertRaises(ValueError):
            MyInt(0)
            MyInt(1.5)
            MyInt("1")

    def test_正負を判定できる(self):
        with self.subTest("正の場合"):
            self.assertFalse(MyInt(1).is_negative())

        with self.subTest("負の場合"):
            self.assertTrue(MyInt(-1).is_negative())


if __name__ == "__main__":
    unittest.main()
