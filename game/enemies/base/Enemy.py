import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.spritesheet = pygame.image.load('assets/enemies/skeleton_.png').convert_alpha()
        self.image, self.rect, self.collision_rect = self.extract_sprite(0, 24, 24, 32, screen_width, screen_height)
        self.health = 10
        self.speed = 2
        self.weapons_hit_list = set()
        
    def extract_sprite(self, x, y, width, height, screen_width=1280, screen_height=720):
        sprite = pygame.Surface((width, height), pygame.SRCALPHA)
        sprite.blit(self.spritesheet, (0, 0), (x, y, width, height))
        sprite = pygame.transform.scale2x(sprite)
        rect = sprite.get_rect(center=(screen_width // 2, screen_height // 2))
        collision_rect = rect.inflate(-20, -20)
        return sprite, rect, collision_rect
        
    def move(self, player_rect):
        dx, dy = (player_rect.centerx - self.collision_rect.centerx, player_rect.centery - self.collision_rect.centery)
        dist = (dx ** 2 + dy ** 2) ** 0.5 # Euclidean distance
        if dist != 0:
            dx, dy = (dx / dist, dy / dist) # Normalize the vector
            
        self.collision_rect.x += dx * self.speed
        self.collision_rect.y += dy * self.speed
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()
            
    def collision(self, weapon, player_rect):
        if weapon not in self.weapons_hit_list:
            if self.rect.colliderect(weapon.sprite.collision_rect):
                self.take_damage(weapon.sprite.damage)
                self.weapons_hit_list.add(weapon)
        
        if player_rect.colliderect(self.rect):
            print("Player collided with enemy")
        
        
    def update(self, weapon, player):
        player_rect = player.sprite.collision_rect
        self.move(player_rect)
        self.collision(weapon, player_rect)  
        