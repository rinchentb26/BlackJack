from art import logo
import random
from replit import clear

def draw_card():
    """returns a random card from the deck"""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calc_score(hand):
    """returns the score of a player, if 11 is present and sum>21 , it is replaced by 1"""
    if sum(hand)==21 and len(hand)==2:
        return 0
    if 11 in hand and sum(hand)>21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def compare(user_score,comp_score):
    """compares the scores b/w the two players and decides the result"""
    if user_score>21 and comp_score>21:
        return "You both went bust! You lose."
    if (user_score==comp_score):
       return "Same score.It's a draw."
    if user_score==0 or comp_score==0:
        if comp_score!=0:
            return "Blackjack! You won."
        else:
            return "Blackjack for the Dealer! You lose."
    if user_score>comp_score:
        if user_score<22:
            return "You win."
        else:
            return "You went over 21.You lose."
    if user_score<comp_score:
        if comp_score<22:
            return "You lose."
        else:
            return "Dealer went over 21! You win."

def playGame():
        keepPlaying=True
        player_hand=[]
        dealer_hand=[]
        print(logo)
        for _ in range(2):
            player_hand.append(draw_card())
            dealer_hand.append(draw_card())
        while keepPlaying:
            player_score=calc_score(player_hand)
            dealer_score=calc_score(dealer_hand)
            print(f"You drew: {player_hand} Score: {player_score}")
            print(f"Dealer has {dealer_hand[0]}")
            if player_score==0 or dealer_score==0 or player_score>21:
                keepPlaying=False
            else:
                user_wants_to_deal=input("Do you want to draw another card? Type 'y' or 'n' : ").lower()
                if user_wants_to_deal=='y':
                    player_hand.append(draw_card())
                else:
                    keepPlaying=False
        while dealer_score!=0 and dealer_score<17:
            dealer_hand.append(draw_card())
            dealer_score=calc_score(dealer_hand)
        print(f"Your final hand {player_hand} Score:{player_score}")
        print(f"The dealer's final hand {dealer_hand} Score:{dealer_score}")
        print(f"{compare(player_score,dealer_score)}")
while(input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()=="y"):
    clear()
    playGame()

# BlackJack considerations for this program 
# 1) No Jokers
# 2) Equal Probability for each card
# 3) Face Cards count as 10
# 4) Ace can count as 11/1
# 5) If both bust, dealer wins