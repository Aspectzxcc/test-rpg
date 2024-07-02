import pygame
from .base.MeleeWeapon import MeleeWeapon

class Sword(MeleeWeapon):
    def __init__(self, damage, cooldown, range, special_effect):
        super().__init__(damage, cooldown, range)
        self.special_effect = special_effect
        self.image = pygame.image.load('assets/weapons/sword/Animation-1/sprite-0001.png').convert_alpha()
        self.rect = self.image.get_rect()
        
    def render(self, screen, player_rect, player_direction):
        current_time = pygame.time.get_ticks()
        
        if self.is_active(current_time):
            # The sword image is facing up by default
            if player_direction == 'left':
                # Rotate the image 90 degrees clockwise to face left
                sword_image = pygame.transform.rotate(self.image, 90)
                self.rect = sword_image.get_rect(center=player_rect.midleft)  # Position the sword to the left of the player
            elif player_direction == 'right':
                # Rotate the image 270 degrees clockwise (or 90 counter-clockwise) to face right
                sword_image = pygame.transform.rotate(self.image, -90)
                self.rect = sword_image.get_rect(center=player_rect.midright)  # Position the sword to the right of the player
            elif player_direction == 'up':
                # No rotation needed since the sword is already facing up
                sword_image = self.image
                self.rect = sword_image.get_rect(center=player_rect.midtop)  # Position the sword above the player
            elif player_direction == 'down':
                # Rotate the image 180 degrees to face down
                sword_image = pygame.transform.rotate(self.image, 180)
                self.rect = sword_image.get_rect(center=player_rect.midbottom)  # Position the sword below the player
            
            screen.blit(sword_image, self.rect)
            
            # draw bounding box
            # pygame.draw.rect(screen, 'Green', self.rect, 1)
        else:
            self.rect = (0, 0, 0, 0)
            