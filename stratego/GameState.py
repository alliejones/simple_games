from enum import Enum

class GameState(Enum):
    player_setup = -2
    start = -1
    setup = 0
    pieces_placed = 1
    gameplay = 2
    conflict = 3
    win = 4
