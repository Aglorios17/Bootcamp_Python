import sys
import random

secret = random.randint(1, 99)
print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!\n")
i = 0
a = 0
exit = "exit"
NB_ESSAIS_MAX = 0
while True and i == 0:
	print("What's your guess between 1 and 99?")
	b = input(">>")
	if b == exit:
		print("Goodbye!")
		i = 1
	if b.isdigit is False:
		print("That's not a number.")
		i = 1
	if i == 0 and b.isdigit() is True:
		a = int(b)
	if a == 42:
		print("The answer to the ultimate question of life, the universe and everything is 42.\nCongratulations! You got it on your first try!")
		i = 1

	elif a < secret and b.isdigit() is True:
		print("Too low!")
	elif a > secret:
		print("Too high!")
	elif a == secret:
		print("Congratulations, you've got it!\nYou won in",NB_ESSAIS_MAX + 1 ,"attempts!")
		i = 1
	NB_ESSAIS_MAX += 1
