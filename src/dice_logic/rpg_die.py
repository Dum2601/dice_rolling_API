import json
from die import Die

class RpgDices(Die):
    def __init__(self, sides: int = 6, quantity: int = 1, modifiers: list[int] = None):
        super().__init__(sides, quantity)
        self.modifiers = modifiers or []

    def _val_with_modifiers(self):
        modifiers_sum: int = sum(self.modifiers) if self.modifiers else 0
        dice_values = self.die_result
        results = []
        for value in dice_values:
            results.append({
                "die_value": value,
                "modifiers_sum": modifiers_sum,
                "total": value + modifiers_sum
            })
        return json.dumps(results, indent=4)

    @property
    def rpg_dice_with_modifiers(self):
        return self._val_with_modifiers()


# rpg_die = RpgDices(20, 2, modifiers=[-1])
# print(rpg_die.rpg_dice_with_modifiers)
