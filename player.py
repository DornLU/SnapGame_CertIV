from deck import Deck

class Player(Deck):
    def __init__(self, name):
        """Constructs a player object, inherited from the deck class. The player is given a name.
        
        Parameters:
            name (string): The name of the player, used to display their information during events.
        """
        super().__init__()
        self.name = name
        self.outOfPlay = False
        self.winner = False
        self.randomSnapNumber = 0


    def display(self):
        """Displays the name and card count of the player."""
        if (len(self.cards)) == 1:
            outstring = ("{} has {} card left in their hand.".format(self.name, len(self.cards)))
        else:
            outstring = ("{} has {} cards left in their hand.".format(self.name, len(self.cards)))
        return outstring


    def playCard(self, deck):
        """Takes the top most card from the player's hand and places it on top of the deck. Displays this event.
        
        Parameters:
            deck (Deck): A reference to the deck used in the game.
        
        Returns:
            outstring (string): Feeds into Tkinter label text to display in GUI.
        """
        outstring = ("{} places {} of {} to the pile.".format(self.name, self.cards[0].rank, self.cards[0].suit))
        deck.cards.insert(0, self.cards.pop(0))
        return outstring
        # takes top card from hand and inserts to the top of the deck


    def snap(self, deck):
        """The player snaps, taking all the cards from the deck, clearing the deck and shuffling their hand. Displays this event.
        
        Parameters:
            deck (Deck): A reference to the deck used in the game.
        
        Returns:
            outstring (string): Feeds into Tkinter label text to display in GUI.
        """
        self.cards.extend(deck.cards)
        deck.cards.clear() # adds all elements of deck to hand
        self.shuffle() # shuffles hand
        outstring = ("{} snaps!".format(self.name))
        return outstring