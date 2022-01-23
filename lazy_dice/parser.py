import re

from lazy_dice import Die


def parse(expression: str) -> list[Die]:
    """
    Convert a command into a list of die.

    Args:
        example: a command described by ([+-]{0,1}\d*)d(\d+)((?:[+-]\d*)*(?!d)).
    """
    groups = re.findall(r"([+-]{0,1}\d*)d(\d+)((?:[+-]\d*)*(?!d))", expression)
    dice = []
    for group in groups:
        num, val, modifier = parse_die(*group)
        dice.append(Die(num, val, modifier))
    return dice


def parse_die(num: str, val: str, modifier: str) -> tuple[int, int, int]:
    num_conv = {"+": 1, "-": -1, "": 1}
    if num in num_conv:
        num_int = num_conv[num]
    else:
        num_int = int(num)
    val_int = int(val)
    if modifier != "":
        modifier_int = sum([int(x) for x in re.split(r"(?<!^)(?=[\+-])", modifier)])
    else:
        modifier_int = 0
    return num_int, val_int, modifier_int
