import output as o


class Player:
    def __init__(self):
        self.money = 1000
        self.hand = []
        self.bet = 0
        self.total = 0


    def show_cards(self):
        msg = ""
        for x in self.hand:
            msg += x.value.upper() + " and a "
        o.oprint(f"\nYou have a {msg[:-7]}.\n")


    def place_bet(self):
        while True:
            try:
                self.bet = int(input("Enter your bet:\n"))
                if self.money >= self.bet > 0:
                    self.money -= self.bet
                    return
                elif self.bet > self.money:
                    o.error("You don't have enough money to do that.")
                    continue
            except ValueError:
                o.error("Please enter a valid bet.")
                continue
            o.error("Please enter a valid bet.")

    def calc_total(self):
        self.total = 0
        for x in self.hand:
            self.total += x.int_val


    def get_winnings(self):
        self.money += self.bet * 2


    def play(self, deck):
        self.calc_total()
        o.oprint(f"\nYour total is {self.total}")
        while True:
            action = input("Will you hit/stand/double/split/surrender?\n").split(" ")[0].lower()
            if action == "hit":
                self.hit(deck)
                return 0
            elif action == "stand":
                return 1
            elif action == "double":
                self.double(deck)
                return 2
            # elif action == "split":
            #     self.split()
            #     return 3
            elif action == "surrender" and len(self.hand) == 2:
                return 4
            else:
                o.error("Please enter a valid action.")
                continue

    def hit(self, deck):
        self.hand.append(deck.draw())
        self.calc_total()

    def double(self, deck):
        self.money -= self.bet
        self.bet *= 2
        self.hit(deck)
