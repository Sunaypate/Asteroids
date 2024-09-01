# this allows us to use code from
# the open-source pygame library
# throughout this file

def main():
    import constants as con
    import random
    import pygame
    import time
    pygame.init
    import player as py
    framerate = pygame.time.Clock()

    dt = 0

    print("Starting asteroids!")
    print(f"Screen width: {con.SCREEN_WIDTH}")
    print(f"Screen height: {con.SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((con.SCREEN_WIDTH, con.SCREEN_HEIGHT))
    character = py.Player(con.SCREEN_WIDTH / 2, con.SCREEN_HEIGHT / 2)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        character.draw(screen)
        character.update(dt)

        pygame.display.flip()
        framerate.tick(60)
        dt = framerate.tick(60) / 1000

main()





"""


    recta = pygame.Rect(500, 300, 100, 100)
    rectb = pygame.Rect(500, 300, 150, 150)
    rect_c = pygame.Rect(500, 300, 150, 150)

        colors = [ "blue", "red", "purple", "yellow", "pink", "green", "pink", "orange", "brown", "white" ]

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
        

"""