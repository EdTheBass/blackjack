import output as o


class Dealer:
    def __init__(self):
        self.hand = []
        self.total = 0

    def show_card(self):
        card = self.hand[0]
        o.oprint(f"The dealer has a {card.value.upper()}.\n")

    def show_cards(self):
        msg = ""
        for x in self.hand:
            msg += x.value.upper() + " and a "
        o.oprint(f"\nThe dealer had a {msg[:-7]}.\n")

    def deal(self, player, deck):
        player.hand.append(deck.draw())
        player.hand.append(deck.draw())
        player.calc_total()

        self.hand.append(deck.draw())
        self.hand.append(deck.draw())
        self.calc_total()

    def calc_total(self):
        self.total = 0
        for x in self.hand:
            self.total += x.int_val

    def play(self, deck):
        self.calc_total()

        if self.total < 17:
            while self.total < 17 <= 21:
                self.hit(deck)
                return 0
        else:
            return 1

    def hit(self, deck):
        self.hand.append(deck.draw())
        self.calc_total()

