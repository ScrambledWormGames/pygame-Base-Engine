import pygame

from config import HEIGHT, WIDTH, FPS, GameState
from pause import PauseMenu
from start import StartMenu
from player import Player


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        print("Pygame Initialised")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Minimal Game Engine")
        self.pause_menu = PauseMenu()
        self.start_menu = StartMenu()
        self.running = False
        self.game_entities = []
        self.game_entities.append(Player())
        self.clock = pygame.time.Clock()
        self.dt = 0.0
        self.current_state = GameState.START
        self.font = pygame.font.SysFont(None, 48)

    def run(self):
        self.running = True

        while self.running:
            self.dt = self.clock.tick(FPS) / 1000
            self.get_events()

            if not self.running:
                continue

            if self.current_state == GameState.START:
                self.start_menu.update(self.dt)
                self.start_menu.draw(self.screen)

            elif self.current_state == GameState.GAME:
                self.update()
                self.draw()

            elif self.current_state == GameState.PAUSE:
                self.draw()
                self.pause_menu.update(self.dt)
                self.pause_menu.draw(self.screen)

            pygame.display.flip()

    def get_events(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    print("Quitting game")
                    self.running = False
                    return
                case pygame.KEYDOWN:
                    self._handle_keydown(event.key)

    def _handle_keydown(self, key):
        match self.current_state:
            case GameState.START:
                if key == pygame.K_RETURN:
                    self.current_state = GameState.GAME
            case GameState.GAME:
                if key == pygame.K_ESCAPE:
                    self.current_state = GameState.PAUSE
            case GameState.PAUSE:
                if key == pygame.K_ESCAPE:
                    self.current_state = GameState.GAME
                if key == pygame.K_RETURN:
                    if self.pause_menu.selected == 0:
                        self.current_state = GameState.GAME

                    elif self.pause_menu.selected == 1:
                        self._restart()
                        self.pause_menu.selected = 0
                        self.current_state = GameState.GAME

                    elif self.pause_menu.selected == 2:
                        self.running = False
                        return

    def _restart(self):
        for entity in self.game_entities:
            entity.kill()
        self.game_entities.append(Player())

    def update(self):
        # Remove dead entities.
        self.game_entities = [e for e in self.game_entities if e.alive]

        for entity in self.game_entities:
            entity.update(self.dt)

    def draw(self):
        self.screen.fill((0, 0, 0))
        for entity in self.game_entities:
            entity.draw(self.screen)

    def close(self):
        pygame.font.quit()
        pygame.quit()
