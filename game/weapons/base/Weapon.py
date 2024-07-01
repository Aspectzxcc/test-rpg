class Weapon:
    def __init__(self, damage, cooldown):
        self.damage = damage
        self.cooldown = cooldown # Cooldown in milliseconds
        self.last_use_time = 0

    def use(self, current_time, *args, **kwargs):
        if current_time - self.last_use_time < self.cooldown:
            print("Weapon on cooldown")
            return
        print("Weapon used with damage:", self.damage)