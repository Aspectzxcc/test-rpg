import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.spritesheet = pygame.image.load('assets/enemies/slime/slime.png').convert_alpha()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height // 2))
        self.health = 10
        self.speed = 2
        self.weapons_hit_list = set()
        
    def extract_sprite(self, x, y, width, height, screen_width=1280, screen_height=720):
        sprite = pygame.Surface((width, height), pygame.SRCALPHA)
        sprite.blit(self.spritesheet, (0, 0), (x, y, width, height))
        sprite = pygame.transform.scale2x(sprite)
        rect = sprite.get_rect(center=(screen_width // 2, screen_height // 2))
        return sprite, rect
        
    def move(self, player_rect):
        dx, dy = (player_rect.centerx - self.rect.x, player_rect.centery - self.rect.y)
        dist = (dx ** 2 + dy ** 2) ** 0.5 # Euclidean distance
        if dist != 0:
            dx, dy = (dx / dist, dy / dist) # Normalize the vector
            
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
    
    def take_damage(self, damage):
        self.health -= damage
        print(f"Enemy health: {self.health}")
        if self.health <= 0:
            self.kill()
            
    def collision(self, weapon):
        if weapon not in self.weapons_hit_list:
            if pygame.sprite.spritecollide(self, weapon, False):
                self.take_damage(weapon.sprite.damage)
                self.weapons_hit_list.add(weapon)
        
    def update(self, weapon, player_rect):
        self.move(player_rect)
        self.collision(weapon)  
        