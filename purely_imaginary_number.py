from __future__ import annotations

from my_int import MyInt


class 純虚数:
    def __init__(self, 虚部: MyInt):
        self.虚部 = 虚部

    def __str__(self) -> str:
        if self.虚部 == MyInt(1):
            return 'i'

        if self.虚部 == MyInt(-1):
            return '-i'

        return f'{self.虚部}i'

    def __eq__(self, other: 純虚数):
        return isinstance(other, 純虚数) and self.虚部 == other.虚部

    def to_conjugate(self) -> 純虚数:
        return 純虚数(self.虚部.flip())
