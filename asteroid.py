import pygame 
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
         pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle) 

        small_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid = Asteroid(new_velocity1, self.position,small_asteroid_radius)
        new_asteroid.velocity *= 1.2
        new_asteroid2 = Asteroid(new_velocity2, self.position,small_asteroid_radius) 
        new_asteroid2.velocity *= 1.2
