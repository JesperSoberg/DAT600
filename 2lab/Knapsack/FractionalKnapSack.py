def solveFractionalKnapSack(weights: list, prices: list, capacity: int):
	pricesPerKg = []
	for i in range(len(weights)):
		pricePerKg = prices[i]/weights[i]
		pricesPerKg.append((i, pricePerKg))

	pricesPerKg.sort()
	print(pricesPerKg)