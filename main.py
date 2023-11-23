from deck import Deck
from player import Player
import time
import random
import pygame
from pygame.locals import *

pygame.init()
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FONT = pygame.font.SysFont(None, 24)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

textList = []

def game(event):
    # Setting up the game
    # Instantiates deck
    deck = Deck()
    # Creates and add all cards to deck
    deck.create()
    # Shuffle deck
    deck.shuffle()
    # Create an empty list of players
    players = []
    # Take input of how many players are playing. Min is 2 and max is 8 players
    playerCount = 0
    while playerCount < 2 or playerCount > 8:
        try:
            playerCount = int(input("How many players? (2-8 allowed): "))
        except:
            textList.append(FONT.render("Not a valid number. Please input a number between 2 and 8."))
            continue
        if playerCount > 8:
            textList.append(FONT.render("Too many players. Please input a number between 2 and 8."))
        elif playerCount < 2:
            textList.append(FONT.render("Not enough players. Please input a number between 2 and 8."))
    # Take inputs of player's names for as many players in playerCount.
    for i in range(playerCount):
        while event.key != K_RETURN:
            playerName = ""
            textList.append(FONT.render("Enter player {}'s name: ".format(i+1)))
            if event.type == KEYDOWN:
                textList[len(textList)-1] += event.unicode
                playerName += event.unicode
            for x in range(len(textList)):
                SCREEN.blit(textList[x], (0,x))
        # playerName = input("Enter player {}'s name: ".format(i+1))
        players.append(Player(playerName))
    # Deal equal number of cards to players
    deck.deal(players)

    # Playing the game
    # Start game - when gameWin is true, the game will end.
    gameWin = False
    while gameWin == False:
        # Each player takes turns playing a card, blindly from the top of their hand.
        for player in players:
            # Initialise a counter to keep track of players who've lost.
            outOfPlayCount = 0

            # Need to run over the players again, within this turn, to determine if the current
            for xPlayer in players:
                if (xPlayer.outOfPlay == True): # if the players lose state is true...
                    outOfPlayCount += 1        # increment the counter

            # When all but one player is out of cards, end the game
            if outOfPlayCount == len(players)-1: #if only on player is left in play
                for yPlayer in players: 
                    if len(yPlayer.cards) > 0: #find the player with at least 1 card left
                        yPlayer.winner = True #set win state for them to True
                        if yPlayer.winner == True: #if there is a True win state
                            winner = yPlayer #declare that player the winner
                            gameWin = True #end game
                            continue

            # Player can only take their turn if they have not been eliminated
            if player.outOfPlay == False: 
                # Current player plays a card
                player.playCard(deck)
                # Prevents trying to compare against empty deck, like after a snap.        
                if len(deck.cards) > 1:
                # If played card rank matches the rank of the top card on the deck
                    if deck.cards[0].rank == deck.cards[1].rank:
                        playerRolls = []
                        # Each player gets a chance to call snap
                            # this will be simulated with a random roll to determine who called snap first
                            # allow only inPlay players to roll
                        for zPlayer in players: #scan through players again
                            if zPlayer.outOfPlay == False: #if they are in play, roll a random number
                                zPlayer.randomSnapNumber = random.randint(1, 32767)
                            else: #else, set roll to minValue
                                zPlayer.randomSnapNumber = 0
                            playerRolls.append((zPlayer, zPlayer.randomSnapNumber))
                        #lambda a:a[1] allows to find the second value in the tuple, the snapNumber
                        #reverse true places highest value at index 0
                        playerRolls.sort(key = lambda a: a[1], reverse= True) 
                        playerSnapped_Tuple = playerRolls[0]
                        # Snap adds all cards from deck to player hand and shuffles
                        playerSnapped = playerSnapped_Tuple[0]
                        playerSnapped.snap(deck)
                # Check if player is out of cards, set lose state to true
                if len(player.cards) == 0:
                    player.outOfPlay = True
            # added delay time to make the game run smoother.
            time.sleep(2)
            
    print("Game over")
    print(winner.name, "is the winner!")
    # playAgain = input("Would you like to play again? y/n: ").lower
    # if playAgain == "n":
        # Add field

def main():
    # pygame.init()

    
    clock = pygame.time.Clock()

    running = True
    
    img = FONT.render('Hello', True, WHITE)
    img = FONT.render('bitch', True, WHITE)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            for x in range(len(textList)):
                SCREEN.blit(textList[x], (0,x))

            pygame.display.update()

    pygame.display.flip()

    clock.tick(60)
    pygame.quit()

if __name__=="__main__":
    main()


# game()
