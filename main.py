import Card 
import Deck
import Player
import Validation


def store_values(winner):
	# Opens the file
	fp = open("Blackjack-Winners.txt", "a")
	# Creates the line of information to be stored.
	line = str(winner.name) + " won with " + str(winner.total_points())
	line += " points\n"
	# Places line in the text file.
	fp.write(line)
	# Closes the text file.
	fp.close()

# Retrieves a list containing lines of information from a text file
def retrieve_values(fileName):
	# Opens the file in a read only mode
	fp = open(fileName, "r")

	# List for storing the information
	informationList = []

	for content in fp:
		# Splits the information using ", " into a list and appends the list to the informationList
		informationList.append(content.split(", "))

	return informationList

# Initializes the drawing deck with all 52 cards.
def createDrawingDeck(): 
	# Retrieves cards from the Deck text file
	drawdeck=retrieve_values("Deck.txt")

	# Initializes the deck variable
	deck=Deck.Deck()

	# Adds cards to the deck
	for card in drawdeck:
		drawcard=Card.Card()
		drawcard.set_values(card[0],card[1],int(card[2]),bool(card[3].strip("\n")))
		deck.add_card(drawcard)
		
	return deck

# Creates a deck containing the player's hand.
def set_players_hand(newPlayer, name):
	playerhand = Deck.Deck()

	# Draws a card and makes it invisible to other players.
	newCard = drawingDeck.draw_card()
	newCard.visible = False
	# If the card is an ace, the user is prompted to choose the point value.
	newCard=newPlayer.setAcePoints(newCard,name)
	# Adds the card to the variable containing the player's hand.
	playerhand.add_card(newCard) 

	# Draws a card and is automatically visible to other players.
	newCard=drawingDeck.draw_card()
	# If the card is an ace, the user is prompted to choose the point value.
	newCard=newPlayer.setAcePoints(newCard,name)
	# Adds the card to the variable containing the player's hand.
	playerhand.add_card(newCard)

	return playerhand
	
# Determines how many players are playing and creates a player object. 
# Automatically adds two cards for the players hand.
# Returns a list containing all of the players.
def getPlayers(drawingDeck):
	playerList = []
	firstplayer=Player.Player()

	# Retrieves players name and makes it capitalized.
	name = input("Please enter name: ").capitalize()
	print()

	# Creates a deck for the player's hand containing two cards. 
	# One card is visible the other is not visible.
	playerhand = set_players_hand(firstplayer, name)

	# Sets the first players value. 
	firstplayer.set_values(1, name, playerhand)
	# Adds the player to the player list.
	playerList.append(firstplayer)

	# Prompts the user to either add a player or begin game.
	print("1-Add Player, 2-Begin Game")
	userchoice = Validation.number_validation([1,2], "Please select: ")

	# Initializes the id value to one since a player has been created.
	id = 1

	# As long as the user selects to add a player the following will occur.
	while userchoice==1:
		# If all of the cards have been drawn then the drawing deck is reset.
		if len(drawingDeck.cards) == 0:
			drawingDeck = createDrawingDeck()
		# The id is incremented for each player
		id += 1

		# The new player's values are instantiated.
		newplayer=Player.Player()

		# The user is prompted for a name, which is capitalized.
		name = input("Please enter name: ").capitalize()
		print()
		# Creates a deck for the player's hand containing two cards. 
		# One card is visible the other is not visible.
		playerhand = set_players_hand(newplayer, name)

		# The new player's values are set.
		newplayer.set_values(id, name, playerhand)

		# The new player is appended to the player list.
		playerList.append(newplayer)

		# The user is prompted to either add a player or begin the game.
		print("1-Add Player, 2-Begin Game")
		userchoice = Validation.number_validation([1,2], "Please select: ")
		
	# Now all of the players have been added to the player list.
	# If their is less than two players then a cpu is created.
	if len(playerList)<2:
		# The player object for cpu is instantiated.
		cpu = Player.Player()

		# The name of the cpu is set.
		cpu.name = "Balor the Ictimizer!"

		# A card is drawn for the cpu
		newCard = drawingDeck.draw_card()
		newCard.visible = False

		# If an Ace is drawn the cpu sets its points to 11.
		if newCard.faceValue=="Ace":
			newCard.points=11

		# The card is added to the cpu's hand.
		cpu.cards.add_card(newCard)

		# Another card is drawn.
		newCard = drawingDeck.draw_card()

		# If the card is an Ace, then the cpu determines the card's points
		# through if statements.
		if newCard.faceValue=="Ace":
			# If the cpu's current total points is less than or equal to ten,
			# then the cpu sets the card's points to 11.
			if cpu.total_points()<=10:
				newCard.points=11
			# Otherwise the cpu sets the card's points to 1.
			else:
				newCard.points=1

		# The card is added to the cpu's hand.
		cpu.cards.add_card(newCard)

		# The cpu is added to the player list.
		playerList.append(cpu)
	
	return playerList

# Before any players take their turn the players total points are added
# to determine if any have 21 points or more. 
# If any player has 21 points or more, then the game ends.
def setUpGame(playerList):
	endGame = False
	for player in playerList:
		if player.total_points()>=21:
			endGame=True
	return endGame

# Determines who won and displays the player's points as well as who won.
def displayWinner(playerList):
	winner = ""
	winnerList = []
	# Closest points represents the points closest to 21.
	closestPoints = 0

	for player in playerList:
		# The players total points is found.
		playerstotalpoints=player.total_points()

		# If the players total points is equal to or less than 21,
		# then more if statements are performed to determine if the player
		# has won.
		if playerstotalpoints <= 21:
			# If the players points is greater than the closest points,
			# then they are set as the winner.
			if playerstotalpoints > closestPoints:
				closestPoints = playerstotalpoints
				winnerList = []
				winnerList.append(player)
			# If their points are equal to the closest points,
			# then they are appended to a winner list.
			elif playerstotalpoints == closestPoints:
				winnerList.append(player)

	for winner in winnerList:
		print(winner.name, "Won! With", winner.total_points(), "points")
		store_values(winner)
		for card in winner.cards.cards:
			card.display()
		print()

	# Every other player who did not win is displayed along with
	# their cards.
	for player in playerList:
		if player not in winnerList:
			print(player.name, "had", player.total_points(), "points")
			for card in player.cards.cards:
				card.display()
			print()
				
# This variable determines whether the user is done using the program.
endProgram = False 

# While the end of the program is false. The program will continue.
while endProgram == False:
	# Welcomes the user to the program.
	print("Welcome to Blackjack!")
	print("Empty yer wallet!")
	print("-----------------------")
	print()

	# Creates a drawing deck.
	drawingDeck = createDrawingDeck()

	# Retrieves the players.
	playerList = getPlayers(drawingDeck)
	print()

	# Represents the amount of continues holds.
	holdNumber = 0

	# Determines if the game has ended.
	endGame = setUpGame(playerList)

	# While the game has not ended. The program will cycle through 
	# the players turns.
	while endGame==False:	
		for player in playerList:
			# If the drawing deck is empty, then it is reset with 52 cards.
			if len(drawingDeck.cards) == 0:
				print("New Deck in play")
				print()
				drawingDeck = createDrawingDeck()

			# If the player id equals zero, then the player is a cpu.
			if player.id==0:
				# If the cpu's total points is less than 18,
				# then the cpu draws a card.
				if player.total_points()<18:
					newCard=drawingDeck.draw_card()
					newCard.visible=False

					# If a card drawn is an Ace, then the cpu determines
					# whether the card's points is 1 or 11.
					if newCard.faceValue=="Ace":
						if player.total_points()<=10:
							newCard.points=11
						else:
							newCard.points=1
					player.cards.add_card(newCard)
				# If the cpu's total points is greater than or equal to 18,
				# then the cpu holds.
				else:
					holdNumber+=1
				# If the cpu has more than or equal to 21 points,
				# then the game ends.
				if player.total_points()>=21:
					endGame=True
					break
			# If the player id is not equal to zero,
			# then the player is a user.
			else:
				# The user decides whether they will hold or hit (draw a card).
				# Returns a list containing the value of endGame and holdNumber.
				information = player.players_turn(drawingDeck, playerList)

				# Retrieves the endGame value.
				endGame=information[0]

				# Sets the holdNumber based on the information returned from the
				# player's turn.
				if information[1]==0:
					holdNumber=0
				else:
					holdNumber+=1

				# If the endGame is true, then the game ends.
				if endGame == True:
					break
			# If the holdNumber is the same as the number of players,
			# then the game ends.
			if holdNumber==len(playerList):
				endGame=True
				break

	# The winner is displayed along with the other players.
	displayWinner(playerList)

	# Determines whether the user would like to play again.
	restart=Validation.string_validation(["y","n"], "Gambler! Feeling Lucky? (y or n) ")
	print("------------------------------------------------")
	
	# If the player does not want to play again, then the program ends.
	if restart=="n":
		endProgram=True

	print()