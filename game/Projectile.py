import pygame

class Projectile:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def update(self):
        # Update the projectile's position based on its velocity
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])

    def draw(self, screen):
        # Draw the projectile as a small circle for simplicity
        pygame.draw.circle(screen, (255, 0, 0), self.position, 5)