import pygame
from .base.MeleeWeapon import MeleeWeapon

class Sword(MeleeWeapon):
    def __init__(self, damage, cooldown, range, special_effect):
        super().__init__(damage, cooldown, range)
        self.special_effect = special_effect
        self.image = None
        self.rect = None

    def use(self, current_time, *args, **kwargs):
        super().use(current_time, *args, **kwargs)
        
    def render_sprite(self, screen, player_rect, player_direction):
        current_time = pygame.time.get_ticks()
        
        if current_time - self.last_use_time <= 100:
            self.image = pygame.image.load('assets/weapons/sword-1.png')
            self.image = pygame.transform.rotozoom(self.image, -45, 0.2) 
            
            if player_direction == 'right':
                self.rect = self.image.get_rect(center=(player_rect.right + 10, player_rect.centery))
            elif player_direction == 'left':
                self.image = pygame.transform.flip(self.image, True, False)
                self.rect = self.image.get_rect(center=(player_rect.left - 10, player_rect.centery))
            elif player_direction == 'up':
                self.image = pygame.transform.rotate(self.image, 90)
                self.rect = self.image.get_rect(center=(player_rect.centerx, player_rect.top - 10))
            elif player_direction == 'down':
                self.image = pygame.transform.rotate(self.image, -90)
                self.rect = self.image.get_rect(center=(player_rect.centerx, player_rect.bottom + 10))
            
            screen.blit(self.image, self.rect)
        
    def render(self, screen, player_position, player_direction, current_time):
        if current_time - self.last_use_time <= 100:
            blade_color = (255, 255, 255)  # White blade
            handle_color = (139, 69, 19)  # Brown handle

            # Define sword geometry
            blade_length = 40
            blade_width = 5
            handle_length = 10
            handle_width = 3

            # Adjust blade and handle positions based on the player's direction
            if player_direction == 'left':
                blade = pygame.Rect(player_position[0] - blade_length - handle_length, player_position[1] - blade_width // 2, blade_length, blade_width)
                handle = pygame.Rect(blade.right, player_position[1] - handle_width // 2, handle_length, handle_width)
            elif player_direction == 'right':
                blade = pygame.Rect(player_position[0] + handle_length, player_position[1] - blade_width // 2, blade_length, blade_width)
                handle = pygame.Rect(player_position[0], player_position[1] - handle_width // 2, handle_length, handle_width)
            elif player_direction == 'up':
                blade = pygame.Rect(player_position[0] - blade_width // 2, player_position[1] - blade_length - handle_length, blade_width, blade_length)
                handle = pygame.Rect(player_position[0] - handle_width // 2, blade.bottom, handle_width, handle_length)
            elif player_direction == 'down':
                blade = pygame.Rect(player_position[0] - blade_width // 2, player_position[1] + handle_length, blade_width, blade_length)
                handle = pygame.Rect(player_position[0] - handle_width // 2, player_position[1], handle_width, handle_length)
                
            # Update Rect object to allow collision detection
            self.rect = blade.union(handle)

            # Draw sword
            pygame.draw.rect(screen, blade_color, blade)
            pygame.draw.rect(screen, handle_color, handle)
            
            # render the bounding box
            pygame.draw.rect(screen, 'Green', self.rect, 1)