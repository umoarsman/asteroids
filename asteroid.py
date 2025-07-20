from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255,255,255),
            self.position,
            self.radius,
            2
        )
    
    def update(self, dt):
        self.position += dt * self.velocity

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50) 
            angle_a = self.velocity.rotate(random_angle)
            angle_b = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_a.velocity = angle_a * 1.2

            asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_b.velocity = angle_b * 1.2