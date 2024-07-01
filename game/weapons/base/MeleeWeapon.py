from .Weapon import Weapon

class MeleeWeapon(Weapon):
    def __init__(self, damage, cooldown, range):
        super().__init__(damage, cooldown)
        self.range = range

    def use(self, current_time, *args, **kwargs):
        if current_time - self.last_use_time < self.cooldown:
            print("Melee weapon on cooldown")
            return
        super().use(current_time, *args, **kwargs)
        self.last_use_time = current_time