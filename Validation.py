# Prompts a user and determines if users input is valid.
def string_validation(validStrings, prompt):
	# Retrieves user input and converts to lowercase
	userInput = input(prompt).lower()

	# Prompts user until valid input is entered.
	while userInput not in validStrings:
		print("Invalid input.")
		userInput = input(prompt).lower()

	# Returns valid input.
	return userInput

# Prompts a user and determines if users input is valid.
def number_validation(validNumbers, prompt):
	# Retrieves user input.
	userInput = int(input(prompt))

	# Prompts user until valid input is entered.
	while userInput not in validNumbers:
		print("Invalid input.")
		userInput = int(input(prompt))

	# Returns valid input.
	return userInput