from lazy_dice import Die, Engine, History


def format_engine(engine: Engine) -> str:
    txt = ""
    current_total = 0
    for i, history in enumerate(engine.history):
        command_dice = f"{format_dice(history.dice)}"
        if current_total:
            command_dice += f"{current_total:+d}"
        if i != 0:
            txt += f"Ace: `!{command_dice}`\n"
        txt += format_history(history, command_dice, current_total)
        current_total += history.total
    return txt


def format_history(history: History, command_dice: str, add: int = 0) -> str:
    txt = "```markdown\n"
    txt += f"# {history.total + add}\n"
    flat_rolls = [str(roll) for dice_roll in history.rolls for roll in dice_roll]
    txt += f"Details: [{command_dice} ({' '.join(flat_rolls)})]\n"
    txt += "```\n"
    return txt


def format_dice(dice: list[Die]) -> str:
    if not dice:
        return ""
    txt = str(dice[0])
    for die in dice[1:]:
        txt += format_die(die, val_sign=True)
    return txt


def format_die(die: Die, val_sign=False) -> str:
    if (not val_sign) or die.num < 0:
        return str(die)
    return f"+{str(die)}"
