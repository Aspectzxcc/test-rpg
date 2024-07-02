import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height // 2))
        self.speed = 5
        
    def move(self, player_rect):
        dx = player_rect.x - self.rect.x
        dy = player_rect.y - self.rect.y
        dist = (dx ** 2 + dy ** 2) ** 0.5
        if dist != 0:
            dx, dy = dx / dist, dy / dist # Normalize the vector
            
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        
    def die(self, weapon):
        if pygame.sprite.spritecollide(self, weapon, False):
            self.kill()
        
    def update(self, weapon, player_rect):
        self.move(player_rect)
        self.die(weapon)
        