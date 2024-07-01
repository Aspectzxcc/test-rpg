import pygame
from .base.MeleeWeapon import MeleeWeapon

class Sword(MeleeWeapon):
    def __init__(self, damage, cooldown, range, special_effect):
        super().__init__(damage, cooldown, range)
        self.special_effect = special_effect
        self.image = pygame.Surface((50, 10))  # Create a surface for the sword's image
        self.image.fill((255, 255, 255))  # Fill the sword's image with white color

    def use(self, current_time, *args, **kwargs):
        if current_time - self.last_use_time < self.cooldown:
            print("Sword on cooldown")
            return
        # Implement sword-specific use behavior here
        super().use(current_time, *args, **kwargs)
        self.last_use_time = current_time
        print("Sword special effect:", self.special_effect)
        # Additional sword-specific logic
    
    def render(self, screen, player_position, player_direction, current_time):
        # Only render if the current time is within 200 milliseconds of the last use
        if current_time - self.last_use_time <= 100:
            # Calculate the sword's position based on the player's direction
            if player_direction == 'left':
                position = (player_position[0] - self.image.get_width(), player_position[1])
                image_to_draw = self.image
            elif player_direction == 'right':
                position = (player_position[0], player_position[1])
                image_to_draw = self.image
            elif player_direction == 'up':
                rotated_image = pygame.transform.rotate(self.image, 90)  # Rotate the image 90 degrees
                position = (player_position[0], player_position[1] - rotated_image.get_height())
                image_to_draw = rotated_image
            elif player_direction == 'down':
                rotated_image = pygame.transform.rotate(self.image, 90)  # Rotate the image 90 degrees
                position = (player_position[0], player_position[1] + self.image.get_height())
                image_to_draw = rotated_image
            else:
                position = (player_position[0] + self.image.get_width(), player_position[1])
                image_to_draw = self.image

            screen.blit(image_to_draw, position)