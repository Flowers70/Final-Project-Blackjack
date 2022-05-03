class Card:
	def __init__(self):
		self.suit = ""
		self.faceValue = ""
		self.points = 0
		self.visible = True

	# Sets the cards values
	def set_values(self, suit, faceValue, points, visible):
		self.suit = suit 
		self.faceValue = faceValue 
		self.points = points 
		self.visible = visible

	# Displays the cards face value and suit
	def display(self):
		print(self.faceValue, "of", self.suit)

