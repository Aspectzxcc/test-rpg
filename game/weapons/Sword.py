from .base.MeleeWeapon import MeleeWeapon

class Sword(MeleeWeapon):
    def __init__(self, damage, cooldown, range, special_effect):
        super().__init__(damage, cooldown, range)
        self.special_effect = special_effect

    def use(self, current_time, *args, **kwargs):
        # Implement sword-specific use behavior here
        super().use(current_time, *args, **kwargs)
        print("Sword special effect:", self.special_effect)
        # Additional sword-specific logic