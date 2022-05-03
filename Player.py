import Deck
import Validation
	
class Player:
	def __init__(self):
		self.id = 0
		self.name = ""
		self.cards = Deck.Deck()

	# Sets the player's values
	def set_values(self, playerID, name, cards):
		self.id = playerID
		self.name = name
		self.cards = cards

	# Displays the player's name
	def display(self):
		print(self.name, end='')

	# Returns the users total points
	def total_points(self):
		return self.cards.total_points()

	# Retrieves input from the user determining the
	# Ace cards points.
	def setAcePoints(self, card, name):
		# Determines if the card is an Ace.
		if card.faceValue=="Ace":
			# Displays prompt for user.
			print("For", name + "'s Ace card")
			print("1 - One point \n2 - Eleven points")
			# Retrieves users selection.
			acevalue = Validation.number_validation([1,2], "Yer Choice Gambler! ")
			print()
			# Sets the card's points based on the user's choice.
			if acevalue == 2:
				card.points=11
		
		return card

	# Displays the cards visible to the player. Prompts the user 
	# to either hit (draw a card) or hold (pass their turn).
	def players_turn(self, drawingDeck, playerList):
		# Displays the players name to indicate whose turn it is.
		print(self.name + "'s turn")
		print("--------------------")

		# Creates the endGame variable
		endGame = False

		# Displays the other players' visible cards
		for player in playerList:
			if player.name != self.name:
				print(player.name + "'s cards")
				for card in player.cards.cards:
					if card.visible==True:
						card.display()
				print()

		# Prints the players cards
		print(self.name + "'s cards")
		self.cards.display()
		print(self.name, "has", self.total_points(), "points")

		# Retrieves users choice of action.
		print("1-Hold, 2-Hit")
		playerchoice = Validation.number_validation([1,2], "Yer Choice Gambler! ")		
		print()

		# Determines if the user has chosen to hold.
		hold = 0

		# If the player chose two then a card is drawn.
		if playerchoice==2:
			newcard=drawingDeck.draw_card()
			newcard.visible = False
			newcard=self.setAcePoints(newcard,self.name)
			self.cards.add_card(newcard)
			newcard.display()
			print()

			# Determines if the player has reached or exceeded 21 points.
			if self.total_points() >= 21:
				endGame=True
		else:
			hold=1
			
		# Prints the players total points
		print(self.name + "'s points:", self.total_points())
		print("-------------------------------------")
		print()

		# Returns the endGame variable, which determines if it is the end of the game.
		# Returns the hold variable which determines if the user chose to hold.
		return endGame,hold