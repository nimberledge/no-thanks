"""Class for storage of a turn."""
from enum import Enum

class Turn():
    class Action(Enum):
        PASS_CARD = 0
        TAKE_CARD = 1

    def __init__(self, top_card, counters, player_index, action):
        self.top_card = top_card
        self.counters = counters
        self.player_index = player_index
        self.action = action
