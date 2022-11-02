import random # it will generate a random number
import math
# Taking Inputs for lower bound
A = int(input("Enter  your Lower bound:- "))

# Taking Inputs for upper bound
B = int(input("Enter your Upper bound:- "))

# take random number between A(lower bound) and B(upper bound)
x = random.randint(A, B)
print("\n\tYou've only ", round(math.log(B - A + 1, 2))," chances to guess the number!\n")

# Initializing the number of guesses.
count = 0

# for calculation of minimum number of guesses it's depend upon range

while count < math.log(B - A + 1, 2):
	count += 1

	# taking input of guessing number
	guess = int(input("Guess a number Between A and B:- "))

	# cheching condition
	if x == guess:
		print("Congratulations you did it in ", count, " try")
		# Once you  guessed, the loop will terminate
		break
	elif x > guess:
		print("You guessed number is too small!")
	elif x < guess:
		print("You Guessed number is  too high!")

 #If Guessing is more than required guesses, it will shows the correct number(output).
 
if count >= math.log(B - A + 1, 2):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")

