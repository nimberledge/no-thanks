"""Player abstract base class for No Thanks"""
import abc
import random

class Player(abc.ABC):
    """Player base class, essentially an interface"""

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def start_game(self, num_players, player_index, counters):
        """Setup the start of your game.

        You receive information about the number of players, which player_index you are,
        as well as how many counters you have to begin with."""
        raise NotImplementedError

    @abc.abstractmethod
    def make_turn(self, top_card, counters):
        """Given the top card and the number of counters on it, play a turn.

        Return 0 to pass the card, Return 1 to take it and all counters placed on it.
        If your player has 0 counters and tries to pass, the game engine will flag the illegal move,
        and process the only possible move, i.e. taking the card."""
        raise NotImplementedError

    @abc.abstractmethod
    def see_turn(self, turn):
        """See the latest turn made.

        The information stored here is in the form of a Turn object.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def reset(self):
        """Resets the player at the end of a game."""
        raise NotImplementedError


class RandomPlayer(Player):

    def __init__(self, name):
        super().__init__(name)
        self.num_players = None
        self.idx = None
        self.counters = None
        self.cards = None

    def start_game(self, num_players, player_index, counters):
        self.num_players = num_players
        self.idx = player_index
        self.counters = counters
        self.cards = []

    def make_turn(self, top_card, counters):
        if self.counters == 0:
            return 1
        flip = random.random()
        if flip < 0.6:
            self.counters += counters
            self.cards.append(top_card)
            return 1

        self.counters -= 1
        return 0

    def see_turn(self, turn):
        return

    def reset(self):
        self.num_players = None
        self.idx = None
        self.counters = None
        self.cards = None
