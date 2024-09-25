import circleshape as cs
from constants import SHOT_RADIUS
import pygame

class Shot(cs.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity