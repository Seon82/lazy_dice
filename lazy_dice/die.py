import random
from dataclasses import dataclass


def sign(num: int):
    if num >= 0:
        return 1
    return -1


@dataclass
class Die:
    num: int
    val: int
    modifier: int

    def roll(self) -> list[int]:
        """
        Roll the dice.
        """
        num_sign = sign(self.num)
        return [num_sign * random.randint(1, self.val) for _ in range(abs(self.num))]

    def __str__(self):
        num = "" if self.num == 1 else str(self.num)
        txt = f"{num}d{self.val}"
        if self.modifier:
            txt += f"{self.modifier:+d}"
        return txt
