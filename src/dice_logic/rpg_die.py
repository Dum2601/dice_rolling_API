"""
MIT License

Copyright (c) 2026 Douglas Barbosa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from die import Die

class RpgDices(Die):
    def __init__(self, sides: int = 6, quantity: int = 1, modifiers: list[int] = None):
        super().__init__(sides, quantity)
        self.modifiers = modifiers or []

    def _val_with_modifiers(self):
        _modifiers_sum: int = sum(self.modifiers) if self.modifiers else 0
        _dice_values = self.die_result
        results = []
        for value in _dice_values:
            results.append({
                "die_value": value,
                "modifiers_sum": _modifiers_sum,
                "total": value + _modifiers_sum
            })
        return results

    @property
    def rpg_dice_with_modifiers(self):
        return self._val_with_modifiers()


# rpg_die = RpgDices(20, 2, modifiers=[-1])
# print(rpg_die.rpg_dice_with_modifiers)

# rpg_die = RpgDices(20, 2)
# print(rpg_die.rpg_dice_with_modifiers)