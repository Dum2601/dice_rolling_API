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

import json
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

    @property
    def die_result_json(self):
        _results: list[dict] = []
        _dice_values = self.die_result
        for value in _dice_values:
            _results.append({

                "die_value": value

            })
        return json.dumps(_results, indent=4)


die = Die(6, 3)
print(die.die_result_json)
