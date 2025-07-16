import random

secret_number = random.randint(1,20)

print("I am thinking of a number between 1 and 20.")

guess = 0
guess_taken = 0
for i in range(1, 7):

    guess = int(input("Take a guess!"))

    guess_taken = i

    if guess < secret_number:

        print("Your Guess is too low!")
    
    elif guess > secret_number:

        print("Your Guess is too High!")

    else:

        break;



if guess == secret_number:

	print("Congratulations! , you have got it in {} guesses!".format(str(guess_taken)))

else:

	print("Nope! the number was {}".format(str(secret_number)))
