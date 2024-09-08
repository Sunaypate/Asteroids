import pygame
import random
import constants as con
import time


def rectangle_creator():
    return pygame.Rect(500, 300, 100, 100)


def rectangle_positioner(rect):
    rect.width = random.randrange(10, 200)
    rect.height = random.randrange(10, 200)
    rect.left = random.randrange(0, con.SCREEN_WIDTH - rect.width )
    rect.top = random.randrange(0, con.SCREEN_HEIGHT - rect.height)    

def rectangle_drawer(rect, screen):
    pygame.draw.rect(screen, random.choice(colors), rect)



#colorsold = [ "blue", "red", "purple", "yellow", "pink", "green", "pink", "orange", "brown", "white" ]

colors = ["maroon", "red", "orange", "yellow","green", "cyan", "blue", "indigo", "purple", "white", "brown", "beige", "pink"]
recta = rectangle_creator()
rectb = rectangle_creator()
rect_c = rectangle_creator()

def gameover(screen, framerate):



    for i in range(1, 150):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #screen.fill("black")

        rectangle_positioner(recta)
        rectangle_positioner(rectb)
        rectangle_positioner(rect_c)

        rectangle_drawer(recta, screen)

        rectangle_drawer(rectb, screen)

        rectangle_drawer(rect_c, screen)

        pygame.display.flip()
        framerate.tick(100 - i)
