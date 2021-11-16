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
        if flip < 0.3:
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


class HumanPlayer(Player):

    def __init__(self, name):
        super().__init__(name)

    def start_game(self, num_players, player_index, counters):
        print ("{}'s starting hand".format(self.name))
        print ("num_players: {}".format(num_players))
        print ("your index: {}".format(player_index))
        print ("starting counters: {}".format(counters))
        self.cards = []
        self.counters = counters


    def make_turn(self, top_card, counters):
        self.print_deets()
        print ("Top card: {}, number of counters: {}".format(top_card, counters))
        print ("Enter 1 to take card, Enter 0 to pass on it")
        choice = int(input("Choice? "))
        while choice != 0 and choice != 1:
            print ("invalid choice enter 1 or 0")
            choice = int(input("Choice? "))

        if choice == 0 and self.counters == 0:
            print ("Invalid choice, taking card")
            self.counters += counters
            self.cards.append(top_card)
        elif choice == 0:
            self.counters -= 1
        else:
            self.cards.append(top_card)
            self.counters += counters
        return choice


    def see_turn(self, turn):
        print ("Turn made by player: {}".format(turn.player_index))
        print ("Top card: {}, counter on it: {}, action: {}".format(
            turn.top_card, turn.counters, turn.action
        ))


    def print_deets(self):
        print ("Your cards: {}\nYour counters: {}".format(self.cards, self.counters))


    def reset(self):
        self.num_players = None
        self.idx = None
        self.counters = None
        self.cards = None
