# blackjack
Blackjack CLI game

If you don't know how blackjack works, you should probably google it, but here are the basics.

Before you play, you bet some money, and you will win a certain amount back if you win (this varies a lot).
You are playing against the dealer, and with your cards you are trying to make a total of 21. The number cards are worth their number value, J,Q,K are worth 10, and Ace can be 1 or 11, depending on whether your total will go above 21 (called "going bust") with an Ace valued at 11.
Both you and the dealer start with two cards each. You can only see one of the dealers cards (the upcard). Firstly, you choose whether to hit (pick up another card), stand (end your go and stay with your current hand), double (hit and double your bet), split (if you have two identical value cards you can split them off into separate hands), and surrender (you just give up your hand and lose - you can only do this on your first go). 
This repeats until you either stand, surrender, go bust, or reach 21, and then it's the dealer's turn.
The dealer can only hit and stand, and has to reach a total of 17 (although the exact number varies, it is most commonly 17) or above. 

Whoever has the highest total (without going bust) wins. If you both go bust, then the dealer wins. If you get the same value (assuming it is <=21), then you "push" and your bet is returned. 

