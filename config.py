"""
Provides global configuration items and settings.
"""
from enum import Enum, auto

WIDTH = 800
HEIGHT = 600
FPS = 60


class GameState(Enum):
    """
    Main state machine for the Game
    """
    START = auto()
    GAME = auto()
    PAUSE = auto()
    GAMEOVER = auto()
