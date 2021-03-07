# import random

# chance =3
# while chance > 0:
# 	comp = random.randrange(1,11)
# 	print(comp)
# 	user = int(input('Guess the number : '))
# 	if user == comp:
# 		print("User is Guessed the number is",user)
# 		break
# 	else:
# 		print("Wrong choice")
# 		chance = chance - 1
# 		print("Chance left",chance)




import random

chance =6
while chance > 0:
	comp = random.randrange(1,11)
	print(comp)
	user = int(input('Guess the number : '))
	if user == comp:
		print("User is Guessed the number is",comp)
		break
	elif user > comp:
		print('Think Lower')
		chance = chance - 1
		print("Chance left",chance)
	else:
		print('Thank higher')
		chance = chance - 1
		print("Chance left",chance)

if chance > 0:
	print("User has won the game the secret number was.",comp)
else:
	print("User lost the secret number.",comp)