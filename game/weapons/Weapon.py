class Weapon:
    def __init__(self, damage, cooldown):
        self.damage = damage
        self.cooldown = cooldown
        self.last_use_time = 0

    def use(self, current_time, *args, **kwargs):
        if current_time - self.last_use_time >= self.cooldown:
            self.last_use_time = current_time
            print("Weapon used with damage:", self.damage)
            # Implement generic weapon use behavior here
            # Specific behavior (like creating a projectile) should be implemented in subclasses