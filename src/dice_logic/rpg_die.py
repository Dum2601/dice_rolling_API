from die import Die

class RpgDices(Die):
    def __init__(self, sides: int = 6, quantity: int = 1):
        super().__init__(sides, quantity)



rpg_die = RpgDices(20, 2)
print(rpg_die.die_result)
