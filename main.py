# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import *

def main():
    import pygame
    import time
    pygame.init
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill("black")


   
    while True:
        time.sleep(0.01)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        


        pygame.display.flip()


main()