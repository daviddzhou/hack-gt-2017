import sys

def newGame():
	newName = input("Name for save file: ")
	f= open(str(newName) + ".txt", "w+")
	catType = input("Choose between Nyan Cat, Pusheen, and Doraemon: ")
	validCats = ["Nyan Cat", "Pusheen", "Doraemon"]
	while catType not in validCats:
		print("That's not a valid cat type!")
		catType = input("Choose between Nyan Cat, Pusheen, and Doraemon: ")
	f.write(catType)
	f.close()

	f= open("SaveFiles.txt", "a+")
	length = file_len("SaveFiles.txt")
	f.write(newName + '\n')
	f.close()
	print()
	playGame(catType)

def loadGame():
	f= open("SaveFiles.txt", "r")
	validSaves = f.readlines()
	validSaves = [line.strip() for line in validSaves]
	print("Save Files:")
	printList(validSaves)
	f.close()

	chosenSave = input("Choose a save file: ")
	while chosenSave not in validSaves:
		print("That's not a valid save file!")
		chosenSave = input("Choose a save file: ")

	f= open(chosenSave + ".txt", "r")
	catType = f.read()
	f.close()
	print()
	playGame(catType)


def endGame():
	print("Thanks for playing; goodbye!")
	sys.exit()

def file_len(fname):
	with open(str(fname)) as f:
		return sum(1 for _ in f)

def printList(list):
	for item in list:
		print(item)

def playGame(catType):
	print("Say hi to " + str(catType) + "!")

	if catType == "Nyan Cat":
		#import Nyan Cat image
		play = True
		while play == True:
			print("What would you like to do with Nyan Cat?")
			validActions = ["Pet", "Speak"]
			printList(validActions)
			action = input("Choose an action: ")
			while action not in validActions:
				print("That's not a valid action!")
				action = input("Choose an action: ")

			if action == "Pet":
				print("Nyan Cat lunged forward! It's very happy :)")
				print()
			elif action == "Speak":
				speech = input("Enter what you would like to say to Nyan Cat: ")
				if "cute" in speech:
					print("Nyan Cat blushed! >.<")
				elif "love" in speech:
					print("Nyan Cat is very happy :)")
				else:
					print("Nyan Cat is amused!")

			leave = input("If you would like to exit, type 'Yes': ")
			if leave == "Yes" or leave == "yes":
				print("Thank you for playing!")
				play = False

	elif catType == "Pusheen":
		#import Pusheen image
		play = True
		while play == True:
			print("What would you like to do with Pusheen?")
			validActions = ["Pet", "Speak"]
			printList(validActions)
			action = input("Choose an action: ")
			while action not in validActions:
				print("That's not a valid action!")
				action = input("Choose an action: ")
			if action == "Pet":
				print("Pusheen rolls over! Its fat ripples :D")
				print()
			elif action == "Speak":
				speech = input("Enter what you would like to say to Pusheen: ")
				if "cute" in speech:
					print("Pusheen blushes ever so slightly '.' ")
				elif "love" in speech:
					print("Pusheen blushes greatly! >.<")
				else:
					print("Pusheen blinks.")

			leave = input("If you would like to exit, type 'Yes': ")
			if leave == "Yes" or leave == "yes":
				print("Thank you for playing!")
				play = False


	elif catType == "Doraemon":
		#import Doraemon image
		play = True
		while play == True:
			print("What would you like to do with Doraemon?")
			validActions = ["Pet", "Speak"]
			printList(validActions)
			action = input("Choose an action: ")
			while action not in validActions:
				print("That's not a valid action!")
				action = input("Choose an action: ")

			if action == "Pet":
				print("Doraemon flew upwards! It's very happy :)")
				print()
			elif action == "Speak":
				speech = input("Enter what you would like to say to Doraemon: ")
				if "cute" in speech:
					print("Doraemon smiled! :)")
				elif "love" in speech:
					print("Doraemon is flying to the moon! <3")
				else:
					print("Doraemon jumps!")

			leave = input("If you would like to exit, type 'Yes': ")
			if leave == "Yes" or leave == "yes":
				print("Thank you for playing!")
				play = False


print()
print("Welcome to the Cat Simulator!")
print()
print("New Game")
print("Load Game")
print("Exit")
print()

action = input("Please select an action: ")
validActions = ["New Game", "Load Game", "Exit"]
while action not in validActions:
	print("That's not a valid action!")
	action = input("Please select an action: ")
print()

if action == "New Game":
	newGame()
elif action == "Load Game":
	loadGame()
elif action == "Exit":
	endGame()

