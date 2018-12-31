import unittest


class 純虚数:
    def __init__(self, 虚部: int):
        if not isinstance(虚部, int) or 虚部 == 0:
            raise ValueError('虚部は0ではいけません')
        self.虚部 = 虚部

    def __str__(self) -> str:
        if self.虚部 == 1:
            return 'i'

        if self.虚部 == -1:
            return '-i'

        return f'{self.虚部}i'


class TestComplexNumber(unittest.TestCase):
    def test_純虚数の文字列表現を取得できる(self):
        with self.subTest("虚部 が 4 のとき"):
            self.assertEqual('4i', str(純虚数(4)))

        with self.subTest("虚部 が 1 のとき"):
            self.assertEqual('i', str(純虚数(1)))

        with self.subTest("虚部 が -1 のとき"):
            self.assertEqual('-i', str(純虚数(-1)))

    def test_純虚数の虚部には条件が存在する(self):
        with self.subTest("虚部 が 0 でないこと"):
            with self.assertRaises(ValueError):
                純虚数(0)

        with self.subTest("虚部 が 整数 であること"):
            with self.assertRaises(ValueError):
                純虚数(1.5)


if __name__ == "__main__":
    unittest.main()
