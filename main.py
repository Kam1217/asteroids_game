import pygame
from constants import *
from player import Player
from asteroid import Asteroid

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    
    Player.containers = (updatable_group, drawable_group)   
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    Asteroid.containers = (updatable_group, drawable_group, asteroids_group)
    
    while True:
       for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
       screen.fill(color = "black")
       dt = clock.tick(60) / 1000
       updatable_group.update(dt)
       for sprite in drawable_group:       
         sprite.draw(screen)
       pygame.display.flip()

if __name__ == "__main__":
 main()