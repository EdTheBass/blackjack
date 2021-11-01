import deck as d

money = 1000





def get_bet():
    _bet = 0
    while True:
        try:
            _bet = int(input("Enter your bet:\n"))
            if money > _bet > 0:
                break
            elif _bet >= money:
                print("You don't have enough money to do that.")
                sep_blocks()
                continue
        except ValueError:
            print("Please enter a valid bet.")
            sep_blocks()
            continue
        print("Please enter a valid bet.")
        sep_blocks()
    return _bet


def get_winnings():
    global bet
    return bet * (5/3)



deck = d.Deck()
deck.shuffle()

bet = get_bet()
money -= bet


