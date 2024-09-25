import circleshape as cs
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroids(cs.CircleShape):
    
        def __init__(self, x, y, radius):
                    super().__init__(x, y, radius)
                    

        def draw(self, screen):
            pygame.draw.circle(screen, "white", self.position, self.radius, 2)

        def update(self, dt):
            self.position += self.velocity *  dt

        def split(self):

            def split_ast(angle):
                  ast = Asteroids(self.position[0], self.position[1], new_radius)
                  ast.velocity = angle * 1.2
                  


            self.kill()

            if self.radius <= ASTEROID_MIN_RADIUS:
                return
            else:
                random_angle = random.uniform(20, 50)

                #angle_difference = (50 - (-50)) / 4


                angle_1 = self.velocity.rotate(random_angle)
                angle_2 = self.velocity.rotate(-random_angle)
                #angle_3 = self.velocity.rotate(random_angle * angle_difference + 2)
                #angle_4 = self.velocity.rotate(-random_angle * angle_difference + 4)
                new_radius = self.radius - ASTEROID_MIN_RADIUS

                
                split_ast(angle_1)

                split_ast(angle_2)

                #split_ast(self.velocity)

                #split_ast(angle_3)

                #split_ast(angle_4)
