import pygame

class Player:
    # Initialize the player with speed, image, and position
    def __init__(self, screen_width, screen_height):
        self.speed = 5  # Set the player's movement speed
        self.image = pygame.Surface((50, 50))  # Create a surface for the player's image
        self.image.fill((255, 0, 0))  # Fill the player's image with red color
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height // 2))  # Position the player at the center

    # Update the player's position based on keyboard input
    def update(self, keys):
        # Move left
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        # Move right
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        # Move up
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        # Move down
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed