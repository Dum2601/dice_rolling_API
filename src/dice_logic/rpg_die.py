from src.dice_logic.die import Die

class RpgDices(Die):
    def __init__(self, sides: int = 6, quantity: int = 1, modifiers: list[int] = None):
        super().__init__(sides, quantity)
        self.modifiers = modifiers or []

    def _val_with_modifiers(self):
        _modifiers_sum: int = sum(self.modifiers) if self.modifiers else 0
        results = []
        for value in self.die_result:
            results.append({
                "die_value": value,
                "modifiers_sum": _modifiers_sum,
                "total": value + _modifiers_sum
            })
        return results

    @property
    def rpg_dice_json(self):
        return self._val_with_modifiers()
