from enum import Enum

class GameState(Enum):
   NOT_STARTED = 0
   NOT_OPENED = 1
   INTRUCTIONS = 2
   ROUND_ACTIVE = 3
   ROUND_DONE = 4
   GAME_OVER = 5
