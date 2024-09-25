# this allows us to use code from
# the open-source pygame library
# throughout this file
import constants as con
import random
import pygame
import time
import player as py
import asteroids as ast
import asteroidfield as asf
import gameover as gm
import shot as sh

def main():
    
    framerate = pygame.time.Clock()

    dt = 0

    drawable = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    py.Player.containers = (drawable, updateable)
    ast.Asteroids.containers = (asteroids, drawable, updateable)
    asf.AsteroidField.containers = (updateable)
    sh.Shot.containers = (drawable, updateable, shots)

    print("Starting asteroids!")
    print(f"Screen width: {con.SCREEN_WIDTH}")
    print(f"Screen height: {con.SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((con.SCREEN_WIDTH, con.SCREEN_HEIGHT))
    character = py.Player(con.SCREEN_WIDTH / 2, con.SCREEN_HEIGHT / 2)
    field = asf.AsteroidField()

    timer = 0

    while True:
        timer += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        for asteroid in asteroids:
            if character.collision(asteroid) == True:
                print("Game Over!")
                gm.gameover(screen, framerate)
                print(timer)
                return
            else:
                pass

        for object in drawable:
            object.draw(screen)

        for object in updateable:
            object.update(dt)

        pygame.display.flip()
        framerate.tick(60)
        dt = framerate.tick(60) / 1000

main()