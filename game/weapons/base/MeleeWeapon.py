from .Weapon import Weapon

class MeleeWeapon(Weapon):
    def __init__(self, damage, cooldown, range):
        super().__init__(damage, cooldown)
        self.range = range

    def use(self, current_time, *args, **kwargs):
        # Implement melee-specific use behavior here
        super().use(current_time, *args, **kwargs)
        print("Melee weapon used at range:", self.range)
        # Additional melee-specific logic