"""Python class for a game engine for no-thanks.

Refer README.md for details, but the concept is straightforward enough."""
from player import Player


class GameEngine():
    """Game engine class"""
    DECK = tuple(range(3, 36))
    START_COUNTERS = 11

    def __init__(self, players: list(Player)):
        """Initialize the player list."""
        self.players = list(players)
        self.num_players = len(self.players)
        assert 2 <= self.num_players <= 8
        self.starting_player = -1
        self.player_counters = None
        self.player_cards = None
        self.top_card = None
        self.game_deck = None

    def setup_game(self):
        """
        Setup a game of No Thanks.

        Choose the cards to exclude from the deck, shuffle the deck,
        set up each player's hand.
        """
        pass


    def play_turn(self, player_index):
        """
        Play a turn of No Thanks by querying players[player_index] for their move.
        """
        pass


    def compute_scores(self):
        """
        Calculate each player's score at the end of the game, and reveal the winner
        """
        pass


    def play_game(self):
        """
        Play a whole game of No Thanks.
        """
        pass
