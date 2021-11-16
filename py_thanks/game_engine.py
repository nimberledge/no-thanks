"""Python class for a game engine for no-thanks.

Refer README.md for details, but the concept is straightforward enough."""
import random
from player import HumanPlayer, Player, RandomPlayer
from turn import Turn
import logging


LOG_FMT_STR = "INFO: %(message)s"
logging.basicConfig(filename='debug.txt', format=LOG_FMT_STR, level=logging.INFO)

class GameEngine():
    """Game engine class"""
    DECK = tuple(range(3, 36))
    START_COUNTERS = 11

    def __init__(self, players):
        """Initialize the player list."""
        self.players = list(players)
        self.num_players = len(self.players)
        assert 2 <= self.num_players <= 8
        self.starting_player = -1
        self.player_counters = None
        self.player_cards = None
        self.top_card = None
        self.game_deck = None
        self.current_player = None
        self.turns = None
        self.player_scores = [0 for p in self.players]
        self.top_card_counters = None


    def setup_game(self):
        """
        Setup a game of No Thanks.

        Choose the cards to exclude from the deck, shuffle the deck,
        set up each player's hand.
        """
        # Shuffle the deck, then just remove the first 9 cards
        self.game_deck = list(self.DECK)
        random.shuffle(self.game_deck)
        self.game_deck = self.game_deck[9:]
        logging.info("Generated starting deck.")
        logging.info("Deck length: {}".format(len(self.game_deck)))

        # Give each player an empty hand, and START_COUNTERS counters
        self.player_cards = [[] for p in self.players]
        self.player_counters = [self.START_COUNTERS for p in self.players]

        for i, p in enumerate(self.players):
            p.start_game(self.num_players, i, self.player_counters[i])

        self.starting_player = (self.starting_player + 1) % self.num_players
        self.current_player = self.starting_player
        self.turns = []
        self.top_card = None
        self.top_card_counters = 0
        logging.info("Informed players of their starting # counters.")


    def play_turn(self, player_index):
        """
        Play a turn of No Thanks by querying players[player_index] for their move.

        If a player on 0 counters chooses to pass, the game engine overrides this and makes them
        take the card. Upon processing a turn, the game engine updates all players on what happened
        on the turn.
        """
        logging.info("Asking player {} for their move".format(player_index))
        player = self.players[player_index]
        turn_action = player.make_turn(self.top_card, self.top_card_counters)
        logging.info("Player {} chose {}".format(player_index, Turn.ACTIONS[turn_action]))
        # Flag illegal move
        if turn_action == 0 and self.player_counters[player_index] <= 0:
            turn_action = 1
            logging.info("Player {} made an illegal move.".format(player_index))

        turn = Turn(self.top_card, self.top_card_counters, player_index, Turn.ACTIONS[turn_action])
        if turn_action == 0:  # Player passes the card
            self.player_counters[player_index] -= 1
            self.top_card_counters += 1

        if turn_action == 1: # Player takes the card
            self.player_cards[player_index].append(self.top_card)
            self.player_counters[player_index] += self.top_card_counters

        logging.info("Informing all players of the move made.")
        logging.info("Turn info:\n Top card: {}, Counters: {}, Action: {}".format(
            self.top_card, turn.counters, Turn.ACTIONS[turn_action]
        ))
        logging.info("Player {} cards: {}, counters: {}\n".format(
            player_index, self.player_cards[player_index], self.player_counters[player_index]
        ))
        for p in self.players:
            p.see_turn(turn)

        return turn


    def compute_scores(self):
        """
        Calculate each player's score at the end of the game, and reveal the winner
        """
        for i, player_cards in enumerate(self.player_cards):
            player_cards.sort()
            score = 0
            j = 0
            while j < len(player_cards):
                score += player_cards[j]
                # If cards are in a sequence, don't count higher cards
                while j < len(player_cards) - 1 and player_cards[j+1] == player_cards[j] + 1:
                    j += 1
                j += 1
            self.player_scores[i] = score - self.player_counters[i]
            logging.info("Player {} cards: {}".format(i, player_cards))
            logging.info("Player {} counters: {}".format(i, self.player_counters[i]))
            logging.info("Player {} score: {}".format(i, self.player_scores[i]))


    def play_game(self):
        """
        Play a whole game of No Thanks.

        Returns the index of the winner of the game.
        """
        self.setup_game()
        self.top_card = self.game_deck.pop()
        self.top_card_counters = 0
        logging.info("Starting the game, the top card is {}".format(self.top_card))
        while len(self.game_deck) >= 0:
            turn = self.play_turn(self.current_player)
            if turn.action == 'PASS_CARD':
                self.current_player = (self.current_player + 1) % self.num_players
            else:
                if len(self.game_deck) == 0:
                    break
                self.top_card = self.game_deck.pop()
                self.top_card_counters = 0
                logging.info("New top card is {}".format(self.top_card))

            self.turns.append(turn)
        # End of game
        self.compute_scores()
        return self.player_scores.index(min(self.player_scores))

def main():
    # random.seed(1)
    player1 = RandomPlayer("A")
    player2 = RandomPlayer("B")
    player3 = RandomPlayer("C")
    player4 = HumanPlayer("D")
    players = [player1, player2, player3, player4]
    game_engine = GameEngine(players)
    winner = game_engine.play_game()
    logging.info("The winner was: {}".format(players[winner].name))

if __name__ == '__main__':
    main()