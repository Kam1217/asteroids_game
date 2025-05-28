import pygame
import sys
from constants import *
from shot import Shot
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    
    Player.containers = (updatable_group, drawable_group)   
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    
    Asteroid.containers = (updatable_group, drawable_group, asteroids_group)
    AsteroidField.containers = (updatable_group,)
    asteroid_field = AsteroidField()

    Shot.containers = (shots_group, updatable_group, drawable_group)

    while True:
       for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
       screen.fill(color = "black")
       dt = clock.tick(60) / 1000
       updatable_group.update(dt)
       for asteroid in asteroids_group:
          if asteroid.collides_with(player):
             print("Game Over!")
             sys.exit()
       for sprite in drawable_group:       
         sprite.draw(screen)
       pygame.display.flip()

if __name__ == "__main__":
 main()