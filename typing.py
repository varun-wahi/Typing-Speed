import time
import random

text_list = ["abcdefghijklmnopqrstuvwxyz", "the quick brown fox jumped over the lazy dog"]
print("GAME RULES - Type alphabets in lowercase as fast as you can!\n")


while True:
	error = []
	text = random.choice(text_list)
	print("You have to type: \n",text)
	input("\nPress Enter to start!")
	start = time.time()
	user_text = input("TYPE HERE: ")
	stop = time.time()

	if user_text == text:
		print("Correct!")
		print("Time Taken:", stop - start)
	else:
		print("You entered the text wrong.. Try Again?")
		print("Time Taken:", stop - start)

		for i in range(len(text)):
			if text[i]!=user_text[i]:
				error.append(i)
			else:
				pass
		print(error)

		
		input()

	print("\n-----------------------------\n")


