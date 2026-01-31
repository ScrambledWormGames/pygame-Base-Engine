from enum import Enum, auto

WIDTH = 800
HEIGHT = 600
FPS = 60


class GameState(Enum):
    START = auto()
    GAME = auto()
    PAUSE = auto()
    GAMEOVER = auto()
