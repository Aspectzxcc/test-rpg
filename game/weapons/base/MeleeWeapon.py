from .Weapon import Weapon

class MeleeWeapon(Weapon):
    def __init__(self, damage, cooldown, range):
        super().__init__(damage, cooldown)
        self.range = range