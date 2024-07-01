import pygame
from game.Player import Player

# Define the Game class to encapsulate game initialization, loop, and rendering
class Game:
    # Initialize the game
    def __init__(self):
        pygame.init()  # Initialize all imported pygame modules
        self.screen_width, self.screen_height = 800, 600  # Set screen dimensions
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))  # Create the game window
        self.clock = pygame.time.Clock()  # Create a clock object to control the game's framerate
        self.player = Player(self.screen_width, self.screen_height)  # Create a Player instance
        self.running = True  # Flag to keep the game running

    # Main game loop
    def run(self):
        while self.running:
            self.handle_events()  # Handle events like keyboard input and quitting
            self.update()  # Update the game state (e.g., player position)
            self.render()  # Draw everything to the screen
            self.clock.tick(60)  # Limit the game to 60 frames per second
        pygame.quit()  # Uninitialize all pygame modules

    # Handle events like quitting the game
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    # Update game state
    def update(self):
        keys = pygame.key.get_pressed()  # Get the state of all keyboard buttons
        self.player.update(keys)  # Update the player's position based on input

    # Render the game state to the screen
    def render(self):
        self.screen.fill((0, 0, 0))  # Fill the screen with black
        self.screen.blit(self.player.image, self.player.rect)  # Draw the player to the screen
        pygame.display.flip()  # Update the full display Surface to the screen