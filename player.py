import pygame

from entity import Entity


class Player(Entity):
    def __init__(self):
        self.pos: pygame.Vector2 = pygame.Vector2(0, 0)
        self.hitbox: pygame.Rect = pygame.Rect(self.pos.x, self.pos.y, 10, 10)
        self.vel: pygame.Vector2 = pygame.Vector2(0, 0)
        self.alive: bool = True
        self.speed = 50

    def update(self, dt: float):
        """
        The main update method of the Playet

        :param dt: Delta time
        :type dt: float
        """
        k = pygame.key.get_pressed()

        # since they cancel each other out
        self.vel.x = k[pygame.K_d] - k[pygame.K_a]
        self.vel.y = k[pygame.K_s] - k[pygame.K_w]

        if self.vel.length_squared() > 0:
            self.vel = self.vel.normalize()

        self.pos += self.vel * self.speed * dt

        self.hitbox.topleft = self.pos.xy

    def draw(self, display: pygame.Surface):
        """
        The main draw method of the Player

        :param screen: The main game surface
        :type screen: pygame.Surface
        """
        pygame.draw.rect(display, (255, 0, 0), self.hitbox)

    def kill(self):
        """
        Sets the player to not alive, to be reaped by the main game loop
        """
        self.alive = False
