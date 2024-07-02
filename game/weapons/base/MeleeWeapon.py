from .Weapon import Weapon

class MeleeWeapon(Weapon):
    def __init__(self, damage, cooldown, range):
        super().__init__(damage, cooldown)
        self.range = range

    def use(self, current_time, *args, **kwargs):
        super().use(current_time, *args, **kwargs)