import os
import random
os.system("cls")
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \\/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \\  /|K /\\  |     | '_ \\| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \\/ | /  \\ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\
      |  \\/ K|                            _/ |                
      '------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
	"""Returns a random card from the deck"""
	# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	return random.choice(cards)

def calculate_score(cards):
	"""Take a list of cards and return the score calculated from cards"""
	if sum(cards) == 21 and len(cards) == 2:
		return 0
	if 11 in cards and sum(cards) > 21:
		cards.remove(11)
		cards.add(1)
	return sum(cards)

def compare(user_score, computer_score):
	if user_score == computer_score:
		return "Draw"
	elif computer_score == 0:
		return "Lose, Opponent has Blackjack"
	elif user_score == 0:
		return "Win with a Blackjack"
	elif user_score > 21:
		return "You went over. You lose"
	elif computer_score > 21:
		return "Opponent went over. You win"
	elif user_score > computer_score:
		return "You win"
	else:
		return "You Lose"

play = input("Do you want to play a game of BlackJack? Type 'y' or 'n':")

while play == 'y':
	print(logo)
	user_cards = []
	computer_cards = []
	user_cards = random.sample(cards, 2)
	computer_cards = random.sample(cards, 2)
	user_score = -1
	computer_score = -1
	is_game_over = False
	while not is_game_over:
		user_score = calculate_score(user_cards)
		computer_score = calculate_score(computer_cards)
		print(f"Your cards {user_cards}, current score is {user_score}")
		print(f"computer's first card: {computer_cards[0]}")
		if user_score == 0 or user_score==21 or user_score > 21:
			is_game_over = True
		else:
			user_should_deal = input("Type 'y' ot get another card, type 'n' to pass: ")
			if user_should_deal == 'y':
				user_cards.append(deal_card())
			else:
				is_game_over = True
	
	while computer_score!=0 and computer_score < 17:
		computer_cards.append(deal_card())
		computer_score = calculate_score(computer_cards)
	print(f"Your final hand: {user_cards}, final score: {user_score}")
	print(f"Computer's final hand: {computer_cards}, final_score: {computer_score}")
	print(compare(user_score, computer_score))
	play = input("Do you want to play a game of BlackJack? Type 'y' or 'n':")






