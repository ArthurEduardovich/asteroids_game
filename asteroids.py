import pygame
import random
from circleshape import*
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_corner = random.uniform(20, 50)
            a = self.velocity.rotate(rand_corner)
            b = self.velocity.rotate(-rand_corner)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = a * 1.2
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = b * 1.2
            


        