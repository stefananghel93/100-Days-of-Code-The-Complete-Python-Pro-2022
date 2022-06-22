############### Blackjack Project #####################

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

import random
from replit import clear
from art import logo
# Creating a fuctions that picks a random card form the given list
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
# creating a function that calculates the score based on the picked cards and the rules of the game
def calculate_score(cards):
  # if the the first 2 cards are 11(ace) and 10 than is a blackjack and game should end.
  if sum(cards) ==21 and len(cards) ==2:
    return 0
    # if one of the cards is 11(ace) but sum of all the cards in the list is greatear than 21 than 11(ace) takes the value 1
  if 11 in cards and sum(cards) >21:
    cards.remove(11)
    cards.append(1)
  score = sum(cards)
  return(score)


# creating a function that compares the final scores and decides the winner
def compare(computer,user):
   if computer == user:
     return "It's a draw!"
   elif computer ==0:
     return "You lose! Computer has a Blackjack!" 
   elif user == 0:
     return "You win! You have a Blackjack!"
   elif computer>21:
     return "You win!"
   elif user>21:
     return "You lose!"
   elif user>computer:
     return "You win!"
   else:
     return "You lose!"
# defining a functions play_game() in order to ask the user at the end of the actual game if wants to play again.
def play_game(): 
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False
  # using for loop to loop through the list of cards two times in order to pick 2 random cards and add them to an empty list declared above
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
   
 
  # using while loop to ask the user if wants to pick another card and continue the game by adding another card to his list
  while not is_game_over:
    # calculating the actual scores based on calculate_score() fuction defined earlier and printing the actual cards and score
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f" Your cards: {user_cards}, current score: {user_score}")
    print(f" Computer's first card: {computer_cards[0]}")
  # determining if any of the players user or computer has a blackjack or a score higher than 21 in order to continue or ending the game
    if user_score == 0 or computer_score == 0 or user_score>21:
      is_game_over = True
      # if the game is not ended asking the user if wants to pick another card
    else: 
      user_should_deal = input("Do you want to draw another card? Type 'y' in yes or 'n' if not.")
      # based on the user input adding another card to the list
    if user_should_deal == "y":
      user_cards.append(deal_card())
      print(user_cards)
    else: 
      is_game_over = True
      
    
  # determining the computer strategy based on his cards an score
  # while the computer score is not 0(blackjack) and his total score is less than 17 he should pick another card than calculate his new score and so on until his score is greater than 17 then should stop picking cards.
  while computer_score !=0 and computer_score <17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  print(f" Your final hand: {user_cards}, final score:{user_score}")
  print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
# printing the final statements and the final scores
  print(compare(user_score,computer_score))
 
  
  
# after the game has ended asking the user if wants to play again, clearing the console using the clear() funtions and calling the play_game() functions.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
