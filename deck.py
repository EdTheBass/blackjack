import random as r
from copy import deepcopy


class Card:
    def __init__(self, value, suit, int_val):
        self.value = value
        self.suit = suit
        self.int_val = int_val


class Deck:
    def __init__(self):
        self.deck = []
        self.drawn = []

        for val in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "q", "k", "j", "a"]:
            for suit in ["c", "d", "h", "s"]:
                try:
                    int_val = int(val)
                except ValueError:
                    int_val = 11 if val == "a" else 10
                self.deck.append(Card(val, suit, int_val))

    def shuffle(self):
        deck_cpy = deepcopy(self.deck)
        self.deck = []

        for x in range(len(deck_cpy)):
            self.deck.append(r.choice(deck_cpy))

        del deck_cpy

    def draw(self):
        self.drawn.append(self.deck.pop(-1))
        if not len(self.deck):
            self.deck = self.drawn
            self.drawn = []
        return self.drawn[-1]
