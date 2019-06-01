#Enum?
SUITS = ['Hearts', 'Spades', 'Clubs', 'Diamonds']

def rankNumToString(rank ):
        if rank == 1:
            return "Ace"
        if rank in range(11):
            return str(rank)
        if rank == 11:
            return "Jack"
        if rank == 12:
            return "Queen"
        if rank == 13:
            return "King"

def testPlayable():
    print("Testing the playable method...")
    print("************************************")
    joker = Card('Joker','Joker')
    joker2 = Card('Joker','Joker')
    aceOfClubs = Card('Clubs',1)
    kingOfHearts = Card('Hearts',13)
    queenOfSpades = Card('Spades', 12)
    twoOfDiamonds = Card('Diamonds',2)

    #should all pass
    print("Can I play a Joker on a Joker?")
    print(joker.playable(joker2,1))
    print("====================================")
    print("Can I play a Joker on a King?")
    print(joker.playable(kingOfHearts,1))
    print("====================================")
    print("Can I play a King on a Joker?")
    print(kingOfHearts.playable(joker,1))
    print("====================================")
    print("Can I play a King on an Ace?")
    print(kingOfHearts.playable(aceOfClubs, 1))
    print("====================================")
    print("Can I play an Ace on a King?")
    print(aceOfClubs.playable(kingOfHearts, 1))
    print("====================================")
    print("Can I play a two on an Ace?")
    print(twoOfDiamonds.playable(aceOfClubs, 1))
    print("====================================")
    print("Can I play a King on a Queen?")
    print(kingOfHearts.playable(queenOfSpades, 1))
    print("====================================")
    
    #should all fail
    print("Can I play an Ace on a Queen?")
    print(aceOfClubs.playable(queenOfSpades, 1))
    print("====================================")
    print("Can I play a Queen on an Ace?")
    print(queenOfSpades.playable(aceOfClubs, 1))
    print("====================================")
    print("Can I play a Queen on a Two?")
    print(queenOfSpades.playable(twoOfDiamonds, 1))
    print("====================================")
    
def runTests():
    print("Running tests...")
    testPlayable()

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    
    def __str__(self):
        if self.rank == 'Joker':
            return "Joker"
        else:
            cardString = rankNumToString(self.rank)
            cardString = cardString + " of "
            cardString = cardString + self.suit  
            return  cardString

    def print(self):
        print(self)

    def score(self):
        if (self.rank == 'Joker'):
            return 20
        if (self.rank > 10):
            return 10
        else:
            return self.rank

    def playable(self, otherCard,explain):
        if (self.rank == 'Joker'):
            if explain:
                return("Dude, you can play a Joker anytime.")
            return True
        if (otherCard.rank == 'Joker'):
            if explain:
                return("Dude, you can play anything on a Joker.")
            return True
        if ((self.rank == 1) and (otherCard.rank == 13)):
            if explain:
                return("Yep - Aces are considered one higher than an Kings.")
            return True
        if ((self.rank == 13) and (otherCard.rank == 1)):
            if explain:
                return("Yep - Kings are considered one less than an Ace.")
            return True
        if ((self.rank == otherCard.rank + 1) or (self.rank == otherCard.rank - 1) or (self.rank == otherCard.rank)):
            if explain:
                return("Basic rules, Dude. Come on!")
            return True
        else:
            if explain:
                return("Nope, nope, nope! That's a whole lotta nope!")
            return False

#runTests()