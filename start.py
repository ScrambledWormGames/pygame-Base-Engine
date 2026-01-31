import pygame

from config import WIDTH, HEIGHT


class StartMenu:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 48)

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 20))
        text_surface = self.font.render(
            "Press [Enter] to start", True, (255, 255, 255))
        text_rect = text_surface.get_rect(
            center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text_surface, text_rect)
