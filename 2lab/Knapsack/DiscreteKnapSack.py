def solveDiscreteKnapSackProblem(weights, prices, capacity):

	pricesPerKg = []

	solutions = []

	for i in range(len(weights)):
		pricePerKg = prices[i]/weights[i]
		pricesPerKg.append(i, pricePerKg)

def findOptimal(s1: set, s2: set, capacity):
	if s1 <= s2:
		return s2
	if s2 <= s1:
		return s1
	if s1.weight + s2.weight <= capacity:
		return s1.union(s2)
	if s1.pPrKg >= s2.pPrKg:
		return s1
	return s2

 
	
	
