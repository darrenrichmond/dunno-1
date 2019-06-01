class Hand():
    def __init__(self):
        self.cards = []

    def deal(self,num_cards,deck):
        for n in range(num_cards):
            self.cards.append(deck.flip())

    def print(self):
        print("Cards: ")
        for card in enumerate(self.cards):
            card[1].print()

    def showCards(self):
        cards_string = "Cards: "
        for card in enumerate(self.cards):
            card_string = "[" + str(card[0]) + "]" + str(card[1])
            cards_string = cards_string + card_string
        print(cards_string)

    def __len__(self):
        return len(self.cards)

    def score(self):
        hand_score = 0
        for card in enumerate(self.cards):
            hand_score = hand_score + card[1].score()
        return hand_score