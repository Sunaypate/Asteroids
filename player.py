# from circleshape import *

import circleshape as cs
import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOT_COOLDOWN
import shot as sh

class Player(cs.CircleShape):
        def __init__(self, x, y):
            super().__init__(x, y, PLAYER_RADIUS)
            self.rotation = 0
            self.cooldown = 0
        
        
        def triangle(self):
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
            a = self.position + forward * self.radius
            b = self.position - forward * self.radius - right
            c = self.position - forward * self.radius + right
            return [a, b, c]
            
        def draw(self, screen):
            pygame.draw.polygon(screen, "white", self.triangle(), 2)
        
        def rotate(self, dt):
            self.rotation += PLAYER_TURN_SPEED * dt

        def update(self, dt):
            keys = pygame.key.get_pressed()
            self.cooldown -= dt

            if keys[pygame.K_a]:
                d_t = (dt * -1)
                self.rotate(d_t)

            if keys[pygame.K_d]:
                self.rotate(dt)

            if keys[pygame.K_w]:
                self.movef(dt)

            if keys[pygame.K_s]:
                self.moveb(dt)
            
            if keys[pygame.K_SPACE]:
                self.shoot()

        def movef(self, dt):
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position += forward * PLAYER_SPEED * dt

        def moveb(self, dt):
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position -= forward * PLAYER_SPEED * dt

        def shoot(self):
            if self.cooldown > 0:
                pass
            else:
                bullet = sh.Shot(self.position[0], self.position[1])
                velocity = pygame.Vector2(0, 1).rotate(self.rotation)
                velocity *= PLAYER_SHOOT_SPEED
                bullet.velocity = velocity
                self.cooldown = PLAYER_SHOT_COOLDOWN

                
