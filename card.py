class Card:
    def __init__(self, rank, value, suit):
        """Constructs a card object.
        Parameters:
            rank (string): The descriptive value of the card; Ace, 2 through 10, Jack, Queen, King.
            value (int): The numerical value of the card; 1 through 13.
            suit (string): The suit of the card; Hearts, Diamonds, Clubs, Spades.
        """
        self.rank = rank
        self.value = value
        self.suit = suit
    
    def describeCard(self):
        """Displays the information of a given card in plain English."""
        print(self.rank, "of", self.suit, ", value:", self.value)

    

# rank: name of card (jack, nine, etc)
# value: value of card (11, 9, etc)
# suit: suit of card (clubs, diamonds, etc)

# function to show full name of card ("jack of clubs")