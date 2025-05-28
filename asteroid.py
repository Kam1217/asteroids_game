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
        print("Split method called!")
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            print("Small asteroid - returning early")
            return
        small_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        print(f"Creating new asteroids with radius: {small_asteroid_radius}")
        print(f"Current asteroid position: {self.position}")
        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle) * 1.2
        new_velocity2 = self.velocity.rotate(-random_angle) * 1.2

        new_asteroid = Asteroid(self.position.x, self.position.y, small_asteroid_radius) 
        new_asteroid.velocity = new_velocity1
        new_asteroid2 = Asteroid(self.position.x, self.position.y, small_asteroid_radius) 
        new_asteroid2.velocity = new_velocity2
