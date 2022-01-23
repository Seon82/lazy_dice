from dataclasses import dataclass, field

from lazy_dice.die import Die


@dataclass(frozen=True)
class History:
    """
    Represents a group of dice and the result obtained
    by rolling them.

    Args:
        dice: the list of dice that were rolled.
        rolls: the rolls that were obtained.
    """

    dice: list[Die]
    rolls: list[list[int]]
    total: int = field(init=False)

    def __post_init__(self) -> None:
        total = sum(sum(roll) for roll in self.rolls) + sum([die.modifier for die in self.dice])
        # Frozen dataclasses won't let us modify their attributes, even in __post__init__
        object.__setattr__(self, "total", total)


class Engine:
    """
    An object used to run a rolling simulation, including the rethrowing
    mechanism.

    Args:
        dice: The initial list of dice to be thrown.

    Attributes:
        history: A list of history objects representing the current state of the throw.
        total: The current tally of the dice throws.
    """

    def __init__(self, dice: list[Die]) -> None:
        self._dice: list[Die] = dice
        self.history: list[History] = []

    @property
    def total(self):
        return sum(h.total for h in self.history)

    def is_done(self) -> bool:
        """
        Determine whether all the rethrows have been done.
        """
        return self._dice != []

    def _get_rerolls(self, rolls: list[list[int]]) -> list[Die]:
        new_dice = []
        for die, roll in zip(self._dice, rolls):
            reroll = roll.count(die.val)
            if reroll:
                new_dice.append(Die(reroll, die.val, 0))
        return new_dice

    def step(self):
        """
        Run one step of the simulation, and update the history.
        """
        rolls = [die.roll() for die in self._dice]
        history = History(self._dice, rolls)
        self.history.append(history)
        self._dice = self._get_rerolls(rolls)

    def step_until_done(self):
        """
        Run the entire simulation, until all rethrows are done.
        """
        while self._dice:
            self.step()
