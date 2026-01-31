"""
The main game hub.  Most things stem from this file.
"""
import pygame

from config import HEIGHT, WIDTH, FPS, GameState
from pause import PauseMenu
from start import StartMenu
from player import Player


class Game:
    """
    The main game object.
    """
    def __init__(self):
        """
        Game object initialisation
        """
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
        """
        Starts the main game loop and implements event, update and draw methods.
        """
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
        """
        Handles main game events
        """
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    print("Quitting game")
                    self.running = False
                    return
                case pygame.KEYDOWN:
                    self._handle_keydown(event.key)

    def _handle_keydown(self, key):
        """
        Handles keydown events within the game object.  
        Used primarily for game state alterations. 

        :param key: The pressed key
        :type key: pygame.event.key
        """
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
        """
        Restarts game entities and state
        """
        for entity in self.game_entities:
            entity.kill()
        self.game_entities.append(Player())

    def update(self):
        """
        The main update method for the game.
        Triggers updates in all attached entities.
        """
        # Remove dead entities.
        self.game_entities = [e for e in self.game_entities if e.alive]

        for entity in self.game_entities:
            entity.update(self.dt)

    def draw(self):
        """
        The main draw method for the game.
        Triggers draw in all attached entities.
        """
        self.screen.fill((0, 0, 0))
        for entity in self.game_entities:
            entity.draw(self.screen)

    def close(self):
        """
        Ensures pygame shuts down cleanly
        """
        pygame.font.quit()
        pygame.quit()
