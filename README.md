# no-thanks
Quick little game based on a Tom Scott video - https://www.youtube.com/watch?v=TaFTKRjMY68

Obviously I take no credit for the game concept. Just thought it made for an interesting game, and I want to try making up nice strategies for it. 

## Rules of the game
* Disclaimer that the game may need balancing if there are more or fewer than 4 players
1. All players start with 11 "counters" or small black beads
2. The game deck consists of cards labeled 3 - 35, with 9 cards randomly excluded from the deck
3. The first player begins by removing the top card from the deck. They are then faced with a choice to either
    - Take the card
    - Place a counter on the card and pass the turn to the next player
4. If a player takes a card, they receive the card and all the beads placed on it. They must also draw the next card from the deck, and are allowed the earlier two options again.
5. If a player has no counters, they must pick up the card in front of them.
6. The game ends when all cards have been picked up. A player's score is the sum of the numbers on their cards minus the number of counters in their hand.
7. If a player has a run of consecutive cards, only the lowest card in the run counts towards their score (e.g. if someone picks up the 22, 21, and 20 cards, only the 20 counts towards their total). 
8. The player with the lowest overall score wins the game.

## Outline of work
1. First step I will probably write a Python game engine so I can work out quirks in design and stuff
2. Next step is to port the game itself into Javascript using Boardgame.io
3. Step after that is to create a nice little front-end so that we can play online
4. Last step will probably be creating a game lobby, which I still have to figure out how to do

Let's see how this pans out. If you're reading this, I've probably made _some_ headway on this.
