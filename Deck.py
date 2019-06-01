import random
from Card import Card
from Hand import Hand
from pprint import pprint

SUITS = ['Hearts', 'Spades', 'Clubs', 'Diamonds']


def createSingleDeck(numJokers):
    deck_array = [(suit, rank) for suit in SUITS for rank in range(1,14)]
    for _ in range(numJokers):
        deck_array.append(('Joker','Joker'))
    return deck_array

class Deck():
    def __init__(self,jokers_per_deck):
        first_deck = createSingleDeck(jokers_per_deck)
        second_deck = createSingleDeck(jokers_per_deck)
        self.deck = first_deck + second_deck
        random.shuffle(self.deck)

    def __len__(self):
        return len(self.deck)
        
    def print(self):
        cards_in_deck = len(self.deck)
        print("This deck has " + str(cards_in_deck) + " cards.")
        #print out the first 10 cards
        for n in range(11):
            print("Card " + str(n) + ": " + str(self.deck[n]))

    def flip(self):
        card_tuple = self.deck.pop(0)
        flipped_card = Card(card_tuple[0],card_tuple[1])
        return flipped_card

    def dealHand(self, num_cards):
        player_hand = Hand()
        player_hand.deal(num_cards,self)
        return player_hand

def testDeck():
    ddeck = Deck(2)
    ddeck.print()
    #flip the first card
    first_card = ddeck.flip()
    print(first_card)
    second_card = ddeck.flip()
    print(second_card)

    hand1 = ddeck.dealHand(3)
    print("Hand 1:")
    hand1.print()
    hand2 = ddeck.dealHand(3)
    print("Hand 2:")
    hand2.print()

#testDeck()