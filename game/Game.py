import pygame
from .Player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width, self.screen_height = 1280, 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.running = True
        
        # player sprite
        self.player = pygame.sprite.GroupSingle(Player(self.screen_width, self.screen_height))

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys)

    def render(self):
        self.screen.fill((200, 200, 200))
        self.player.draw(self.screen)
        self.player.sprite.render(self.screen) # render the player's weapon
        pygame.display.flip()