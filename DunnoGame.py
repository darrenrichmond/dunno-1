import random
from pprint import pprint
from Player import Player
from Round import Round

CARDS_PER_PLAYER = 3
HIGHEST_CARD = 14
JOKERS_PER_DECK = 2
NUM_DECKS = 2
NUM_PLAYERS = 0
NUM_ROUNDS = 0
SHOW_DECK = 0
AUTO_PLAY = False
suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
#suits = ['Pentacles', 'Wands', 'Swords', 'Coins']

class DunnoGame():
    def __init__(self):
        self.cards_per_player = CARDS_PER_PLAYER
        self.jokers = JOKERS_PER_DECK
        self.num_decks = NUM_DECKS
        self.num_players = NUM_PLAYERS
        self.num_rounds = NUM_ROUNDS
        self.players = []
        self.auto_play = AUTO_PLAY

    def getPlayers(self):
        if NUM_PLAYERS == 0:
            print("How many players?")
            self.num_players = int(input())
            p_string = "Players: "
            for p in range(self.num_players):
                player_num = p + 1;
                print("What is the name of player number " + str(player_num) + "?")
                p_name = str(input())
                p_string = p_string + p_name + " "
                player = Player(p_name)
                self.players.append(player)
            print(p_string)

    def getNumRounds(self):
        if NUM_ROUNDS == 0:
            print("How many rounds? [0 for random]")
            self.num_rounds = int(input())
            if self.num_rounds == 0:
                self.num_rounds = random.randint(1,11)
            print("OK, we'll play " + str(self.num_rounds) + " rounds. Lowest score wins!!")
      
    def printFinalScores(self):
        print("Final scores: ")
        for p in enumerate(self.players):
            player = p[1]
            player_name = player.name
            player_score = str(player.total_score)
            print(player_name + ": " + player_score)


    def play(self):
        print("Welcome to Dunno - a fast-paced card game for 2-6 players.")
        self.getPlayers()
        self.getNumRounds()
        for r in range(self.num_rounds):
            dunno_round = Round(self.players, self.cards_per_player, self.jokers)
            dunno_round.play()
        self.printFinalScores()

game = DunnoGame()
game.play()