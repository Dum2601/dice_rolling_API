from random import randint

class Die:
    def __init__(self, sides: int = 6, quantity: int = 1):
        self.sides = sides
        self.quantity = quantity

    def _dice_value(self) -> int:
        return randint(1, self.sides)

    def _all_dice_values(self) -> list[int]:
        values: list[int] = []
        for _ in range(self.quantity):
            values.append(self._dice_value())
        return values

    def _rolling_dices(self) -> list[int]:
        return self._all_dice_values()
    @property
    def die_result(self) -> list[int]:
        return self._rolling_dices()




# die = Die().die_result
# print(die)
