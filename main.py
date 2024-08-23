# this allows us to use code from
# the open-source pygame library
# throughout this file
from constants import *

import random

def main():
    import pygame
    import time
    pygame.init
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    recta = pygame.Rect(500, 300, 100, 100)
    rectb = pygame.Rect(500, 300, 150, 150)
    rect_c = pygame.Rect(500, 300, 150, 150)

    while True:
        colors = [ "blue", "red", "purple", "yellow", "pink", "green", "pink", "orange", "brown", "white" ]
        time.sleep(0.001)
        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return




        # recta.inflate_ip( 1, 1 )
        recta.width = random.randrange(10, 200)
        recta.height = random.randrange(10, 200)
        recta.left = random.randrange(0, SCREEN_WIDTH - recta.width )
        recta.top = random.randrange(0, SCREEN_HEIGHT - recta.height)
        
        


        pygame.draw.rect(screen, random.choice( colors ), recta)

        rectb.width = random.randrange(10, 200)
        rectb.height = random.randrange(10, 200)
        rectb.left = random.randrange(0, SCREEN_WIDTH- rectb.width)
        rectb.top = random.randrange(0, SCREEN_HEIGHT- rectb.height)
        
        pygame.draw.rect(screen, random.choice( colors ), rectb)

        rect_c.width = random.randrange(10, 200)
        rect_c.height = random.randrange(10, 200)
        rect_c.left = random.randrange(0, SCREEN_WIDTH- rect_c.width)
        rect_c.top = random.randrange(0, SCREEN_HEIGHT- rect_c.height)

        pygame.draw.rect(screen, random.choice( colors ), rect_c)
        

        pygame.display.flip()
        
        '''
        pygame.Rect(recta).inflate(100, 100)

        rectb = pygame.Rect(recta)
        rectb.inflate( 100, 100 )
        '''

class Rect:
    def __init_( self, x, y, h, w ):
        pass

    def inflate( self, x, y ):
        return Rect( x, y, self.h, self.w )
        


main()