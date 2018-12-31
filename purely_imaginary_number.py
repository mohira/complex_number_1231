from __future__ import annotations


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

    def __eq__(self, other: 純虚数):
        return isinstance(other, 純虚数) and self.虚部 == other.虚部

    def to_conjugate(self) -> 純虚数:
        return 純虚数(-1 * self.虚部)
