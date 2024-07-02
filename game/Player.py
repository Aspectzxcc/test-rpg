import pygame
from .weapons.Sword import Sword

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.spritesheet = pygame.image.load('assets/player/down_idle.png').convert_alpha()
        self.image, self.rect, self.collision_rect = self.extract_sprite(0, 0, 64, 64, screen_width, screen_height)
        self.direction = 'right'
        self.health = 100
        self.speed = 5
        self.weapon = Sword(damage=10, cooldown=1000, range=5, special_effect="slash")
        
    def extract_sprite(self, x, y, width, height, screen_width=1280, screen_height=720):
        sprite = pygame.Surface((width, height), pygame.SRCALPHA)
        sprite.blit(self.spritesheet, (0, 0), (x, y, width, height))
        sprite = pygame.transform.scale2x(sprite)
        rect = sprite.get_rect(center=(screen_width // 2, screen_height // 2))
        collision_rect = rect.inflate(-80, -50)
        return sprite, rect, collision_rect
        
    def handle_input(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.collision_rect.x -= self.speed
            self.direction = 'left'
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
            self.collision_rect.x += self.speed
            self.direction = 'right'
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.collision_rect.y -= self.speed
            self.direction = 'up'
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
            self.collision_rect.y += self.speed
            self.direction = 'down'

    def update(self, keys):
        self.handle_input(keys)

    def render_weapon(self, screen):
        self.weapon.render(screen, self.rect, self.direction)