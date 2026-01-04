from random import randint

class Dice:
    def __init__(self, dice_sides: int = 6, has_modifiers: bool = False):
        self.dice_sides = dice_sides
        self.has_modifiers = has_modifiers
        self._modifiers = []  

    def rolling_dice(self):
        return randint(1, self.dice_sides)

    @property
    def modifiers(self):
        return sum(self._modifiers)

    @modifiers.setter
    def modifiers(self, modifiers_values: list[int]):
        self._modifiers = modifiers_values

    @property
    def dice_values(self):
        return f"Valor do dado: {self.rolling_dice()} \nValor dos modificadores: {self.modifiers}"
        
dado = Dice(20)
dado.modifiers = [1,2,3]  # Definindo modificadores
print(dado.dice_values)  # Exibe o valor do dado somado aos modificadores

