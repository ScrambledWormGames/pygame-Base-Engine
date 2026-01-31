from enum import Enum, auto

WIDTH = 800
HEIGHT = 600
FPS = 60


class GameState(Enum):
    """
    Provides easier manipulation of the Game state machine
    """
    START = auto()
    GAME = auto()
    PAUSE = auto()
    GAMEOVER = auto()
