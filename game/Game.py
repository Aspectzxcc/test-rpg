import pygame
from random import randint
from .Player import Player
from .enemies.base.Enemy import Enemy

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width, self.screen_height = 1280, 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.enemy_spawn_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.enemy_spawn_timer, 1000)  # Spawn an enemy every second
        
        # sprites
        self.player = pygame.sprite.GroupSingle(Player(self.screen_width, self.screen_height))
        self.weapon = pygame.sprite.GroupSingle(self.player.sprite.weapon)
        self.enemies = pygame.sprite.Group(Enemy(200, 500), Enemy(1000, 100))

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
            if event.type == self.enemy_spawn_timer:
                print("Spawning enemy")
                self.enemies.add(Enemy(randint(0, self.screen_width), randint(0, self.screen_height)))
                
    def collision_detection(self):
        # Check for collisions between player weapon and enemy
        for enemy in self.enemies.sprites():
            if pygame.sprite.spritecollide(enemy, self.weapon, False):
                print("Enemy hit!")
                enemy.die()

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys)
        self.collision_detection()

    def render(self):
        self.screen.fill((200, 200, 200))
        self.player.draw(self.screen)
        self.player.sprite.render_weapon(self.screen)
        self.enemies.draw(self.screen)
        pygame.display.flip()