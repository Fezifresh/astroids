# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

import os 
#Text anzeigen

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    pygame.font.init()
    # Schrift aktivieren

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    # sets the screen size

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #creating groups

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable) 
    #adding classmembers to the groups

    asteroidfield = AsteroidField()

    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    clock = pygame.time.Clock()
    dt = 0
    # sets up the clock for framerate and a delta variable
    
    score = 0
    font = pygame.font.Font(None, 36)
    # sets up initial score and font

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # makes the close-button work
        
        pygame.Surface.fill(screen, (0, 0, 51))
        # opens a dark blue screen
        
        for element in updatable:
            element.update(dt)
        # updates all elements of the group updatable

        for element in drawable:    
            element.draw(screen)
        # draws all elements of the group drawable

        for asteroid in asteroids:
            if asteroid.checkcollision(ship):
                sys.exit("Game over!")
        # Game Over bei Kollision Schiff-Asteroid

        for shot in shots:
            for asteroid in asteroids:
                if shot.checkcollision(asteroid):
                    asteroid.split()
                    shot.kill()
                    score += SCORE_INCREMENT
        # Asteroiden verschwinden bei Treffer

        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
        # refreshes the screen
        
        dt = clock.tick(60) / 1000
        # FPS = 60

        

if __name__ == "__main__":
    main()