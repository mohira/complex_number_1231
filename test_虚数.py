import unittest

from purely_imaginary_number import 純虚数


class 虚数:
    def __init__(self, 実部: int, 虚部: int):
        if not isinstance(実部, int) or 実部 == 0:
            raise ValueError('実部は0ではいけません')

        self.実部 = 実部
        self.純虚数 = 純虚数(虚部)

    def __str__(self) -> str:
        if self.純虚数.虚部 < 0:
            return f'{self.実部}{self.純虚数}'

        return f'{self.実部}+{self.純虚数}'


class Test虚数(unittest.TestCase):
    def test_純虚数の文字列表現を取得できる(self):
        with self.subTest("実部 が 3 かつ 虚部 が 2 のとき"):
            self.assertEqual('3+2i', str(虚数(実部=3, 虚部=2)))

        with self.subTest("実部 が 3 かつ 虚部 が -2 のとき"):
            self.assertEqual('3-2i', str(虚数(実部=3, 虚部=-2)))

    def test_虚数の実部には条件が存在する(self):
        with self.subTest("実部 が 0 でないこと"):
            with self.assertRaises(ValueError):
                虚数(実部=0, 虚部=2)

        with self.subTest("実部 が 整数 であること"):
            with self.assertRaises(ValueError):
                虚数(実部=1.5, 虚部=2)


if __name__ == "__main__":
    unittest.main()
