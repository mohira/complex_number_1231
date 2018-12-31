from __future__ import annotations

import unittest

from my_int import MyInt
from purely_imaginary_number import 純虚数


class Test純虚数(unittest.TestCase):
    def test_純虚数の文字列表現を取得できる(self):
        with self.subTest("虚部 が 4 のとき"):
            self.assertEqual('4i', str(純虚数(MyInt(4))))

        with self.subTest("虚部 が 1 のとき"):
            self.assertEqual('i', str(純虚数(MyInt(1))))

        with self.subTest("虚部 が -1 のとき"):
            self.assertEqual('-i', str(純虚数(MyInt(-1))))

    def test_純虚数の同一性を判定できる(self):
        with self.subTest('虚部 が 等しければ 同一である'):
            self.assertEqual(純虚数(MyInt(2)), 純虚数(MyInt(2)))

        with self.subTest('虚部 が 異なれば 同一でない'):
            self.assertNotEqual(純虚数(MyInt(-2)), 純虚数(MyInt(2)))

    def test_共役な純虚数を取得できる(self):
        with self.subTest("2i の 共役は -2i"):
            self.assertEqual(純虚数(MyInt(-2)), 純虚数(MyInt(2)).to_conjugate())

        with self.subTest("-2i の 共役は 2i"):
            self.assertEqual(純虚数(MyInt(2)), 純虚数(MyInt(-2)).to_conjugate())

        with self.subTest("i の 共役は -i"):
            self.assertEqual(純虚数(MyInt(-1)), 純虚数(MyInt(1)).to_conjugate())

        with self.subTest("-i の 共役は i"):
            self.assertEqual(純虚数(MyInt(1)), 純虚数(MyInt(-1)).to_conjugate())


if __name__ == "__main__":
    unittest.main()
