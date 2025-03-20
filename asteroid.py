import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rangle = random.uniform(20, 50)
            vector1 = self.velocity.rotate(rangle)
            vector2 = self.velocity.rotate(-rangle)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_rad)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_rad)
            asteroid1.velocity = vector1 * 1.2
            asteroid2.velocity = vector2 * 1.2        
