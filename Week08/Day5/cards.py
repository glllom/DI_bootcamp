import random


class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for value in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.cards.append(Card(suit, value))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


new_deck = Deck()
print(list(map(lambda card: (card.suit, card.value), new_deck.cards)))
for _ in range(50):
    print(new_deck.deal().suit)
print(list(map(lambda card: (card.suit, card.value), new_deck.cards)))
