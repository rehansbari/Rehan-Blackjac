import random
from art import logo
from replit import clear
############### Blackjack Project #####################

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
  random_card = random.choice(cards)
  return random_card

def calculate_score(cards):
  score = sum(cards)

  if len(cards) == 2 and 11 in cards and score == 21:
    score = 0

  if 11 in cards and score > 21:
    cards.remove(11)
    cards.append(1)
    score = sum(cards)
  return score

def compare(user_total, computer_total):
  if user_total == computer_total:
    print("Draw")
  elif computer_total == 0:
    print("You lose computer had a blackjack")
  elif user_total == 0:
    print("You win! You had a blackjack")
  elif computer_total > 21:
    print("You win")
  elif user_total > computer_total and user_total < 21:
    print("You win since you had a higher score")
  elif computer_total > user_total:
    print("You lose the computer had a higher score")
  
def play_game():
  user_cards = []
  computer_cards = []
  user_cards.append(deal_card())
  user_cards.append(deal_card())
  computer_cards.append(deal_card())
  computer_cards.append(deal_card())

  print(f"Your hand is {user_cards}")
  print(f"The computers first card is {computer_cards[0]}")

  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  print(f"Your total is {user_score}")

  game_finished = False
  while game_finished == False:
    if user_score == 0 and computer_score == 0 or user_score > 21:
      print("You lose")
      game_finished = True
    else:
      add_card = input("Would you like to draw another card? y or n: ").lower()

      if add_card == 'y':
        user_cards.append(deal_card())
        print(user_cards)
        user_score = calculate_score(user_cards)
        print(f"Your score is {user_score}")
      else:
        game_finished = True

      while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

  compare(user_score, computer_score)
  print(f" Your final hand {user_cards} with a total of: {user_score}")
  print(f" The computers final hand {computer_cards} with a total of: {computer_score}")
    
user_wants_to_play = input("Do you wanto to play a game of blackjack? Type 'y' or 'n' ").lower()

while user_wants_to_play != 'n':
  play_game()
  user_wants_to_play = input("Do you want to to play again? Type 'y' or 'n' ").lower()
  if user_wants_to_play == 'y':
    clear()
    print(logo)
