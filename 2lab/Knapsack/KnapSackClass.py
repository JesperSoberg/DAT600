class KnapSack:

	def __init__(self, weight, price, ids):
		self.weight = weight
		self.price = price
		self.pPrKg = price / weight
		self.ids = ids

	def __lt__(self, otherSet):
		return self.ids < otherSet.ids
	
	def __le__(self, otherSet):
		return self.ids <= otherSet.ids
	
	def __gt__(self, otherSet):
		return self.ids > otherSet.ids
	
	def __ge__(self, otherSet):
		return self.ids >= otherSet.ids