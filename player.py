from constants import *
from circleshape import *
from shot import Shot

class Player(CircleShape):
    
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.color = PLAYER_COLOR
        self.immunity = False
        self.shield_activation_time = 0
        self.shield_duration = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0:
            return
        new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN

    def activate_shield(self, time):
        self.color = (255, 255, 0)
        self.immunity = True
        self.shield_activation_time = pygame.time.get_ticks()
        self.shield_duration = time

    def deactivate_shield(self):
        self.color = PLAYER_COLOR
        self.immunity = False

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.triangle(), 2)

    def update(self, dt):
        self.timer -= dt
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(0 - dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(0 - dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
            
    