import pygame

from config import WIDTH, HEIGHT


class StartMenu:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 48)

    def update(self, dt):
        """
        The update method for StartMenu
        **Currently unused**

        :param dt: Delta time
        :type dt: float
        """
        pass

    def draw(self, screen):
        """
        The draw method for StartMenu

        :param screen: The main game surface
        :type screen: pygame.Surface
        """
        screen.fill((0, 0, 20))
        text_surface = self.font.render(
            "Press [Enter] to start", True, (255, 255, 255))
        text_rect = text_surface.get_rect(
            center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text_surface, text_rect)
