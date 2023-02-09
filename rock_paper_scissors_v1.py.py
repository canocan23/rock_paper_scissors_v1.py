from random import randint

computer_wins = 0
player_wins = 0
winning_score = 3

while computer_wins < winning_score and player_wins < winning_score:
	player1 = input("your choice ")
	if player1 == "quit" or player1 == "q":
		break
	computer = randint(0,2)

	if computer == 0:
		computer = "rock"
	if computer == 1:
		computer = "paper"
	if computer == 2:
		computer = "scissors"
	print(f"computer plays {computer}")

	if player1 == computer:
		print("its even")
		print(f"player:{player_wins} vs computer:{computer_wins}")
	elif player1 == "rock":
		if computer == "scissors":
			player_wins = player_wins + 1
			print("you win")
			print(f"player:{player_wins} vs computer:{computer_wins}")
		else:
			computer_wins = computer_wins + 1
			print("computer wins")
			print(f"player:{player_wins} vs computer:{computer_wins}")
	elif player1 == "paper":
		if computer == "rock":
			player_wins = player_wins + 1
			print("you win")
			print(f"player:{player_wins} vs computer:{computer_wins}")
		else:
			computer_wins = computer_wins + 1
			print("computer wins")
			print(f"player:{player_wins} vs computer:{computer_wins}")
	elif player1 == "scissors":
		if computer == "paper":
			player_wins = player_wins + 1
			print("you win")
			print(f"player:{player_wins} vs computer:{computer_wins}")
		else:
			computer_wins = computer_wins + 1
			print("computer wins")
			print(f"player:{player_wins} vs computer:{computer_wins}")
	else:
		print("ERROR")
if player_wins > computer_wins:
	print("Player has won the competition")
elif computer_wins > player_wins:
	print("Computer has won the competition")
else:
	print("Its a tie !")

