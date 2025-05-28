import pygame
from circleshape import CircleShape

class Bullet(CircleShape):
     def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
     
     def draw(self, screen):
        pass
    
     def update(self, dt):
        pass
     
     def collides_with(self, other):
        pass