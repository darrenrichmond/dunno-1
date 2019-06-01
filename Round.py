from Deck import Deck
from Player import Player
from pprint import pprint

class Round():
    def __init__(self, players, cards_per_player, jokers_per_deck):
        self.deck = Deck(jokers_per_deck)
        self.players = players
        self.cards_per_player = cards_per_player

    def deal(self):
        for player in enumerate(self.players):
            player[1].dealHand(self.deck, self.cards_per_player)

    def describe(self):
        print("Here are the " + str(len(self.players)) + " players:")
        for player in enumerate(self.players):
            player[1].print()
        print("There are " + str(len(self.deck)) + " cards left in the deck")

    def no_winner(self):
        for player in enumerate(self.players):
            if player[1].is_winner():
                return False
        return True

    def score(self):
        for player in enumerate(self.players):
            player[1].score()

    def play(self):
        self.deal()
        top_card = self.deck.flip()
        print("Here we go!")
        print("*********************************")

        while self.no_winner():
            for player in enumerate(self.players):
                top_card = player[1].takeTurn(top_card,self.deck)
                if(self.no_winner() == False):
                    print("Winner of this round is " + player[1].name + "!")
                    self.score()
                    break
                print("---------------------------------")
            print("*********************************")    

def testRound():
    #create the players
    players = []
    darren = Player("Darren")
    players.append(darren)
    eron = Player("Eron")
    players.append(eron)
    #create the round with default values
    round1 = Round(players, 1, 2)
    #deal the cards and describe what everyone has
    round1.deal()
    round1.play()
        
#testRound()