import pygame

from config import WIDTH, HEIGHT


class PauseMenu:
    def __init__(self):
        self.options: list = [
            "Resume",
            "Restart",
            "Quit Game"
        ]
        self.selected: int = 0
        self.overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.font = pygame.font.SysFont(None, 48)

    def update(self, dt):
        k = pygame.key.get_just_pressed()
        if k[pygame.K_DOWN]:
            if self.selected < len(self.options) - 1:
                self.selected += 1
            else:
                self.selected = 0

        if k[pygame.K_UP]:
            if self.selected > 0:
                self.selected -= 1
            else:
                self.selected = len(self.options) - 1

    def draw(self, screen):
        self.overlay.fill((0, 0, 120, 50))
        screen.blit(self.overlay, (0, 0))

        header_surface = self.font.render(
            "Paused", True, (255, 255, 255))
        header_rect = header_surface.get_rect(
            center=(WIDTH // 2,
                    (HEIGHT // 2) - (50 * (len(self.options) + 2))))
        screen.blit(header_surface, header_rect)

        for i, opt in enumerate(self.options):
            bg_col = (255, 0, 0) if i == self.selected else None
            opt_surface = self.font.render(
                opt, True, (255, 255, 255), bg_col)
            opt_rect = opt_surface.get_rect(
                center=(WIDTH // 2,
                        (HEIGHT // 2) - (50 * (len(self.options) - (i + 1)))))
            screen.blit(opt_surface, opt_rect)
