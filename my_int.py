from __future__ import annotations


class MyInt:
    def __init__(self, int_num: int):
        if not isinstance(int_num, int) or int_num == 0:
            raise ValueError('0以外の整数でなればなりません')

        self.value = int_num

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, other: MyInt) -> bool:
        return isinstance(other, MyInt) and self.value == other.value

    def __lt__(self, other: MyInt) -> bool:
        return self.value < other.value

    def is_negative(self) -> bool:
        return self.value < 0

    def flip(self) -> MyInt:
        return MyInt(-1 * self.value)
