"""Class for storage of a turn."""
from enum import Enum

class Turn():
    ACTIONS = ['PASS_CARD', 'TAKE_CARD']

    def __init__(self, top_card, counters, player_index, action):
        self.top_card = top_card
        self.counters = counters
        self.player_index = player_index
        self.action = action
