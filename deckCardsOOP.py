from random import shuffle

class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value


class Deck:
	def __init__(self, cards):
		self.cards = cards

	def deal(self):
		return self.cards.pop(0)

	def shuffle(self):
		if len(self.cards) == 52:
			shuffle(self.cards)
			print("Deck shuffled")
		else:
			print("Deck is not full")

