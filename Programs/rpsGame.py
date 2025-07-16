import random, sys

print("ROCK, PAPER, SCISSORS")

win_count = 0

lose_count = 0

tie_count = 0



#while loop to start the Game

while True:

	print("{} Wins, {} Losses, {} Ties ".format(win_count, lose_count, tie_count))

#while loop to start the player game

	while True:

		user_input = input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit ")

		if user_input == 'q':

			sys.exit()

		if user_input == "r" or user_input == "p" or user_input == "s":

			break #breaks out of player loop

	#Display what the player choose

	if user_input == "r":

		print("ROCK versus ...")

	elif user_input == "p":

		print("PAPER versus ...")

	elif user_input == "s":

		print("SCISSORS versus ...")



#Display what computer choose

	move_value = random.randint(1,3)
	computer_input = None  # Ensure computer_input is always defined

	if move_value == 1:

		computer_input = "r"

		print("ROCK")

	elif move_value == 2:

		computer_input = "p"

		print("PAPER")

	elif move_value == 3:

		computer_input = "s"

		print("SCISSORS")


	# Display and record the win/loss/tie:

	if user_input == computer_input:
		print("It is a tie!")
		tie_count += 1
	elif user_input == "r" and computer_input == "s":
		print("You Win!")
		win_count += 1
	elif user_input == "p" and computer_input == "r":
		print("You Win!")
		win_count += 1
	elif user_input == "s" and computer_input == "p":
		print("You Win!")
		win_count += 1
	elif user_input == "s" and computer_input == "r":
		print("You Lose!")
		lose_count += 1
	elif user_input == "r" and computer_input == "p":
		print("You Lose!")
		lose_count += 1
	elif user_input == "p" and computer_input == "s":
		print("You Lose!")
		lose_count += 1
