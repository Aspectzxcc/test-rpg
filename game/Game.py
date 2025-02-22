import pygame
from random import randint
from .Player import Player
from .enemies.base.Enemy import Enemy

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width, self.screen_height = 1280, 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Game")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # sprites
        self.player = pygame.sprite.GroupSingle(Player(self.screen_width, self.screen_height))
        self.weapon = pygame.sprite.GroupSingle(self.player.sprite.weapon)
        self.enemies = pygame.sprite.Group()
        
        # timers
        self.enemy_spawn_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.enemy_spawn_timer, 1000)  # Spawn an enemy every second
        self.weapon_use_timer = pygame.USEREVENT + 2
        pygame.time.set_timer(self.weapon_use_timer, self.weapon.sprite.cooldown)  # Use weapon every second (for testing)

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
            if event.type == self.weapon_use_timer:
                print("Using weapon")
                for enemy in self.enemies.sprites():
                    enemy.weapons_hit_list.clear()
                self.weapon.sprite.use(pygame.time.get_ticks())

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys)
        self.enemies.update(self.weapon, self.player)    
        
    def draw_bounds(self):
        pygame.draw.rect(self.screen, 'Black', self.player.sprite.rect, 1)
        pygame.draw.rect(self.screen, 'White', self.player.sprite.collision_rect, 1)
        pygame.draw.rect(self.screen, 'Red', self.weapon.sprite.rect, 1)
        pygame.draw.rect(self.screen, 'Green', self.weapon.sprite.collision_rect, 1)
        for enemy in self.enemies:
            pygame.draw.rect(self.screen, 'Red', enemy.rect, 1)
            pygame.draw.rect(self.screen, 'Green', enemy.collision_rect, 1)

    def render(self):
        self.screen.fill((200, 200, 200))
        self.player.draw(self.screen)
        self.player.sprite.render_weapon(self.screen)
        self.enemies.draw(self.screen)
        
        # draw bounding boxes for debugging
        self.draw_bounds()
        
        pygame.display.flip()