from card import Card
import random

class Deck():
    def __init__(self):
        """Constructs a deck object. Contains the data needed to make a deck of 52 cards."""
        self.cards = []
        self.rank = ["Ace", "2", "3", "4", "5", "6", "7",
                     "8", "9", "10", "Jack", "Queen", "King"]
        self.suit = ["Clubs", "Spades", "Hearts", "Diamonds"]
    
    def getDeck(self):
        """Gets the data of the cards currently in the deck.
        
        Returns:
            cards (list): A collection of all cards currently in the deck.
        """
        return self.cards
    
    def create(self):
        """Creates a deck by looping through each suit within a loop of each rank.
        The current loop iteration for each is combined to form the card.
        The card is then added to the list of cards.
        """
        for rank in self.rank:
            for suit in self.suit:
                value = self.rank.index(rank) + 1 # ace at index 0, + 1 to get value 1
                self.cards.append(Card(rank, value, suit))

    def display(self):
        """Displays information of all cards in the deck in plain English."""
        for x in range(len(self.cards)):
            print(self.cards[x].describeCard())

    def shuffle(self):
        """Shuffles the list of cards."""
        random.shuffle(self.cards)

    def deal(self, players): # where players is a list
        """Repeats through each player, giving them a card until there are either no cards left to give,
        or until giving any more cards would result in uneven distribution among players.

        Parameters:
            players (list): A reference to each player currently in the game.
        """
        lastPlayer = players[len(players)-1] # store data of the last player in the list
        deckLength = len(self.cards) # store deck length
        while (len(lastPlayer.cards) < (deckLength // len(players))):
        # loop until the last player has recieved as many cards as they can
            for player in players: # loop each player
                player.cards.append(self.cards.pop(0)) # add a card to player, removed from deck