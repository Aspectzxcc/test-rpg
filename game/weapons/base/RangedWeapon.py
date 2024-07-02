from .Weapon import Weapon

class RangedWeapon(Weapon):
    def __init__(self, damage, cooldown):
        super().__init__(damage, cooldown)
        self.projectile = None