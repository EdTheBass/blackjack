import deck as d
import player as p
import dealer as de
import output as o


deck = d.Deck()
dealer = de.Dealer()
player = p.Player()

deck.shuffle()

while player.money >= 0:
    o.sep_blocks()

    o.oprint(f"You currently have £{player.money}.")
    player.place_bet()

    dealer.deal(player, deck)

    player.calc_total()
    dealer.calc_total()

    player.show_cards()
    dealer.show_card()

    while True:
        if player.total == 21 or dealer.total == 21:
            break

        p_play = player.play(deck)

        if p_play == 0:
            o.oprint(f"\nYou hit and got a {player.hand[-1].value.upper()}.")
        elif p_play == 1:
            o.oprint(f"\nYou stood.")
        elif p_play == 2:
            o.oprint(f"\nYou doubled and got a {player.hand[-1].value.upper()}, raising your bet to {player.bet}.")
        elif p_play == 3:
            o.oprint(f"\nYou split. Dunno what to put here seeing as splitting doesn't work yet.")
        elif p_play == 4:
            o.oprint(f"\nYou surrendered.")

        if player.total >= 21 or p_play == 1 or p_play == 4:
            ace = False
            for x in player.hand:
                if x.value == "a":
                    ace = True if x.int_val == 11 else False
                    if ace:
                        x.int_val = 1
                        break
            if not ace:
                break

    while True:
        d_play = dealer.play(deck)

        if d_play == 0:
            o.oprint(f"The dealer hit.")
        elif d_play == 1:
            o.oprint(f"The dealer stood.")

        if dealer.total >= 17:
            break

    dealer.show_cards()

    if (dealer.total < player.total <= 21) or (player.total <= 21 < dealer.total):
        o.oprint(f"Yay! You beat the dealer and won {player.bet*2}.")
        player.get_winnings()
    else:
        o.oprint(f"You lost to the dealer.")


    cash_in = input(f"\nCash in your {player.money}? (y/n)\n").lower()[0]
    if cash_in == "y":
        o.sep_blocks()
        o.oprint(f"\nCongrats! You beat the casino for {player.money - 1000}.")
        quit()
    else:
        o.oprint("\nOkay, carrying on.")

    for x in player.hand:
        if x.value == "a":
            x.int_val = 11

    player.hand = []
    dealer.hand = []


o.oprint("Welp, you ran out of money.")
