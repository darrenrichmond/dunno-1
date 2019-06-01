class Player():
    def __init__(self,name):
        self.name = name
        self.total_score = 0

    def dealHand(self, deck, num_cards):
        hand = deck.dealHand(num_cards)
        self.hand = hand

    def print(self):
        print("Player: " + self.name)
        self.hand.print()

    def showCards(self):
        self.hand.showCards()

    def score(self):
        hand_score = self.hand.score()
        print(self.name + " scored " + str(hand_score) + "!")
        self.total_score = self.total_score + hand_score
        return hand_score


    def getPlayerAction(self, prompt, top_card):
        while True:
            #get the action as a string to decide flip or play
            action = input(prompt)
            if (action == 'f'):
                print("You want to flip.")
                return -1
            #it's not a flip - figure out the card they want to play
            else:
                #check if they have valid input
                try:
                    action = int(action)
                except ValueError:
                    print("Input must be f or a number.")
                    continue
                #we have a number - make sure it is in the right range
                max_ = len(self.hand.cards)
                if ((action < 0) or (action > max_)):
                    print("You can't play a card you don't have.")
                    continue
                #check if the card is playable
                selected_card = self.hand.cards[action]
                if (selected_card.playable(top_card,0) == False):
                    print("You can't play that card.")
                    continue
                #player picked a playable card
                return action

    def takeTurn(self, top_card, deck):
        print("The top card is a " + str(top_card))
        print(self.name + ", here is what is in your hand:")
        self.showCards()
        action = self.getPlayerAction("Play a card by entering the number in front of the card to play, or Flip by entering the letter f.", top_card)
        # -1 from getPlayerAction means a flip
        if (action == -1):
            top_card = deck.flip()
            print("You flipped and got a " + str(top_card))
        else:
            card_played = self.hand.cards.pop(action)
            top_card = card_played
            print("You played your " + str(card_played) + ".")
        return top_card

    def is_winner(self):
        return (len(self.hand) == 0)