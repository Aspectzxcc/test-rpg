import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self, damage, cooldown):
        super().__init__()
        self.damage = damage
        self.cooldown = cooldown  # Cooldown in milliseconds
        self.last_use_time = 0
        
    def is_ready(self, current_time):
        return current_time - self.last_use_time >= self.cooldown

    def use(self, current_time, *args, **kwargs):
        if not self.is_ready(current_time):
            return
        self.last_use_time = current_time
