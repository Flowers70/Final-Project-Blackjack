import random


class Deck:
	def __init__(self):
		self.cards = []

	# Adds a card to the deck
	def add_card(self, card):
		self.cards.append(card)

	# Draws a random card from the deck.
	def draw_card(self):
		randomIndex = random.randrange(len(self.cards))
		card = self.cards[randomIndex]
		self.cards.pop(randomIndex)
		return card

	# Calculates the total points of the deck.
	def total_points(self):
		total = 0
		for card in self.cards:
			total += card.points
		return total

	# Displays all of the cards in the deck.
	def display(self):
		for card in self.cards:
			card.display()
		print()