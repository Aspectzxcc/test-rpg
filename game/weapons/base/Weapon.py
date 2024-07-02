import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self, damage, cooldown):
        super().__init__()
        self.image = pygame.Surface((10, 50))
        self.rect = self.image.get_rect()
        self.damage = damage
        self.cooldown = cooldown  # Cooldown in milliseconds
        self.last_use_time = 0
        self.active_duration = 100  # Duration in milliseconds for which the weapon is active
        
    def is_ready(self, current_time):
        return current_time - self.last_use_time >= self.cooldown
    
    def is_active(self, current_time):
        return current_time - self.last_use_time <= self.active_duration

    def use(self, current_time):
        if not self.is_ready(current_time):
            return
        self.last_use_time = current_time
