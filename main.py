# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    # sets the screen size

    clock = pygame.time.Clock()
    dt = 0
    # sets up the clock for framerate and a delta variable

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # makes the close-button work
        
        pygame.Surface.fill(screen, (0, 0, 51))
        # opens a black screen
        pygame.display.flip()
        # refreshes the screen

        dt = clock.tick(60) / 1000
        # FPS = 60

if __name__ == "__main__":
    main()