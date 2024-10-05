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
    font_big = pygame.font.Font(None, 72)
    # sets up initial score and font

    player_immunity = False
    collision_time = 0
    # für inv Frames

    player_health = PLAYER_STARTING_HEALTH

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

        if pygame.time.get_ticks() - collision_time > 1000:
            ship.deactivate_shield()

        for asteroid in asteroids:
            if asteroid.checkcollision(ship):
                if player_health > 0 and ship.immunity == False:
                    player_health -= 1
                    ship.activate_shield()
                    collision_time = pygame.time.get_ticks()
                elif ship.immunity == True:
                    pass
                else:
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
        # aktualisiert die score anzeige

        health_text = font.render(f'Shields: {player_health}', True, (255, 255, 255))
        screen.blit(health_text, (1100, 10))
        
        if player_immunity == True:
            PLAYER_COLOR = (255, 255, 0)

        pygame.display.flip()
        # refreshes the screen
        
        dt = clock.tick(60) / 1000
        # FPS = 60

        

if __name__ == "__main__":
    main()