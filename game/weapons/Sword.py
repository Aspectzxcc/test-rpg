import pygame
from .base.MeleeWeapon import MeleeWeapon

class Sword(MeleeWeapon):
    def __init__(self, damage, cooldown, range, special_effect):
        super().__init__(damage, cooldown, range)
        self.special_effect = special_effect
        self.image = pygame.image.load('assets/weapons/sword/Animation-1/sprite-0001.png').convert_alpha()
        self.rect = self.image.get_rect()

    def use(self, current_time, *args, **kwargs):
        super().use(current_time, *args, **kwargs)
        
    def render_sprite(self, screen, player_rect, player_direction):
        current_time = pygame.time.get_ticks()
        
        if current_time - self.last_use_time <= 100:
            # The sword image is facing up by default
            if player_direction == 'left':
                # Rotate the image 90 degrees clockwise to face left
                sword_image = pygame.transform.rotate(self.image, 90)
                self.rect = self.image.get_rect(midright=player_rect.midleft)  # Position the sword to the left of the player
            elif player_direction == 'right':
                # Rotate the image 270 degrees clockwise (or 90 counter-clockwise) to face right
                sword_image = pygame.transform.rotate(self.image, -90)
                self.rect = self.image.get_rect(midleft=player_rect.midright)  # Position the sword to the right of the player
            elif player_direction == 'up':
                # No rotation needed since the sword is already facing up
                sword_image = self.image
                self.rect = self.image.get_rect(midbottom=player_rect.midtop)  # Position the sword above the player
            elif player_direction == 'down':
                # Rotate the image 180 degrees to face down
                sword_image = pygame.transform.rotate(self.image, 180)
                self.rect = self.image.get_rect(midtop=player_rect.midbottom)  # Position the sword below the player

            # Draw the sword
            screen.blit(sword_image, self.rect)
                
            # Optionally, draw a bounding box around the sword for debugging
            pygame.draw.rect(screen, 'Green', self.rect, 1)
            
        
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