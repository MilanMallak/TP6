from enum import Enum

class GameState(Enum):
   NOT_STARTED = True
   ROUND_ACTIVE = False
   ROUND_DONE = False
   GAME_OVER = False
