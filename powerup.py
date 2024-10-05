from constants import *
from circleshape import *

class Powerup(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, POWER_UP_SIZE)
        

    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
