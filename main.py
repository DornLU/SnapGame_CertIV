from deck import Deck
from player import Player
import time
import random
from tkinter import *
from threading import *

window = Tk()
window.geometry("200x100")

playerCount = 0
newPlayerCount = StringVar()

myList = Listbox()


def gameStart():
    global myList
    gamewindow = Tk()
    gamewindow.geometry("400x300")

    scrollbar = Scrollbar(gamewindow)
    scrollbar.pack(side=RIGHT, fill=Y)
    myList = Listbox(gamewindow, height=400, width=300, yscrollcommand=scrollbar.set, )
    myList.pack(side=LEFT, fill=BOTH)

    t1=Thread(target=game)
    t1.start()
    
    gamewindow.mainloop()


startButton = Button(window,text="Start Game", command = gameStart)


def getPlayerCount():
    global playerCount
    try:
        playerCount = int(newPlayerCount.get())
        startButton.pack() # Generate start button only on valid entry
    except:
        Message(text="ERROR: Not a number. Enter a whole number between 2 and 8.")
        startButton.pack_forget()
    if (playerCount <2):
        Message(text="ERROR: Too low. Enter a whole number between 2 and 8.")
        playerCount = 0
        startButton.pack_forget()
    if (playerCount >8):
        Message(text="ERROR: Too high. Enter a whole number between 2 and 8.")
        playerCount = 0
        startButton.pack_forget()

    
Label(text="How many players? (2-8)").pack()
playerCountEntry = Entry(window, textvariable=newPlayerCount)
playerCountEntry.pack()
Button(text="Confirm",command=getPlayerCount).pack()


def game():
    global playerCount
    global myList
    # Setting up the game
    # Instantiates deck
    deck = Deck()
    # Creates and add all cards to deck
    deck.create()
    # Shuffle deck
    deck.shuffle()
    # Create an empty list of players
    players = []
    # Generate player names and classes
    for i in range(playerCount):
        players.append(Player("Player {}".format(i+1)))
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
                myList.insert(END, player.playCard(deck))
                myList.see(END)
                # Label(text=player.playCard(deck)).pack()
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
                        
                        myList.insert(END, playerSnapped.snap(deck))
                        myList.see(END)
                        
                # Check if player is out of cards, set lose state to true
                if len(player.cards) == 0:
                    player.outOfPlay = True
            # added delay time to make the game run smoother.
            time.sleep(.5)
            
    myList.insert(END, "Game over")
    myList.see(END)
    myList.insert(END, (winner.name + " is the winner!"))
    myList.see(END)
    # playAgain = input("Would you like to play again? y/n: ").lower
    # if playAgain == "n":
        # Add field


window.mainloop()