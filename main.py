from constants import *
import pygame
from player import Player


def main():
    # Initialises pygame
    pygame.init()
    # sets the screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # set the clock variable to the clock object
    clock = pygame.time.Clock()
    dt = 0
   
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2,  SCREEN_HEIGHT / 2)

    # setup the game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       
        updateable.update(dt)

       # creates a black background for the screen
        screen.fill(000)
        
        # Draw the player here
        for obj in drawable:
            obj.draw(screen)
            

        pygame.display.flip()

        # set the framerate to 60fps
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()