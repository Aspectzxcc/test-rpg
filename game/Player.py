import pygame
from .weapons.Sword import Sword

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.speed = 5
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height // 2))
        self.direction = 'right'
        self.weapon = Sword(damage=20, cooldown=1000, range=5, special_effect="slash")
        
    def handle_input(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.direction = 'left'
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
            self.direction = 'right'
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.direction = 'up'
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
            self.direction = 'down'

    def update(self, keys):
        self.handle_input(keys)

    def render_weapon(self, screen):
        self.weapon.render(screen, self.rect, self.direction)