"""Player abstract base class for No Thanks"""
import abc

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

        Must return an object of type Turn.Action i.e.
        Turn.Action.TAKE_CARD if taking the card, or
        Turn.Action.PASS_CARD if passing on the card."""
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
