############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from logo import logo
import random
import os

# Ace는 합계를 고려하여 1, 11로 계산될 수 있음 21이나 11인 경우를 따져 제시할 에이스 값을 결정
# 사용자가 가진 핸드가 10이라면 에이스는 11
# 21이 넘으면 패배 
# Jocker, King, Queen은 10으로 계산 
# 딜러가 가진 핸드 합이 17 미만이면 반드시 카드 한 장을 받아야 한다.
'''
Ace는 1 또는 11로 계산합니다.
King, Queen, Jack은 각각 10으로 계산합니다.
그 외의 카드는 카드에 표시된 숫자로 계산합니다.
Blackjack
처음 두 장의 카드 합이 21일 경우

Bust
카드 합이 21을 초과하면 베팅 금액을 잃게 됩니다.
둘다 버스트이면 딜러 승

Push
플레이어와 딜러의 각각의 카드 합이 같을 경우 서로 비기게 됩니다.

- 게임 규칙 - 
베팅을 한 후 모든 플레이어와 딜러는 두 장의 카드를 받습니다.
딜러는 자신의 카드 중 한 장을 오픈합니다.
딜러는 카드의 합이 17이 될 때까지 반드시 추가 카드를 뽑아야 합니다.
플레이어는 카드의 합이 21을 넘지 않는 범위 내에서 추가 카드를 받을 수도(Hit),받지 않을 수도(Stay)있습니다.
'''



def clear():
    os.system('cls')

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    score = sum(cards)
    return score

def compare(user_score, computer_score):
    # 블랙잭인 경우
    if user_score > 21 and computer_score > 21:
        return "점수를 넘겼습니다. 당신은 패배했습니다."
    if computer_score == 0:
        if user_score == 0:
            return "당신이 블랙 잭 뽑았습니다. 이겼습니다 축하드립니다."
        else:
            return "상대방이 블랙 잭 뽑았습니다. 당신은 패배했습니다."
    elif user_score == 0:
        return "당신이 블랙 잭 뽑았습니다. 이겼습니다. Good."
    elif user_score > 21:
        return "카드합이 21이 넘습니다. 당신은 패배했습니다."
    elif user_score < 21 and computer_score < 21:
        if user_score == computer_score:
            return "비겼습니다."
        elif user_score > computer_score:
            return "당신이 이겼습니다."
        elif user_score < computer_score:
            return "당신이 패배하였습니다."

def start_game():
    user_hand = []
    computer_hand = []
    for _ in range(0,2):
        user_hand.append(deal_card())
        computer_hand.append(deal_card())
    game_over = False
    while not game_over:
        clear()
        print(logo)
        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)
        print(f"    Your cards: {user_hand}, current score: {user_score}")
        print(f"    Computer's first card: {computer_hand[0]}")
        # 블랙잭이면 게임오버
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            hit_or_stay = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit_or_stay == 'y':
                user_hand.append(deal_card())
            else:
                game_over = True
        while computer_score != 0 and computer_score < 17:
            computer_hand.append(deal_card)
            computer
        



while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    start_game()



# 만약 블랙잭을 뽑았을 때 (핸드 합 = 21) 이면 승
# 0 을 반환하면 블랙잭을 나타낸다 




##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

