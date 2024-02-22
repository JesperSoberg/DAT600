def solveFractionalKnapSack(weights: list, prices: list, capacity: int):
	pricesPerKg = []
	for i in range(len(weights)):
		pricePerKg = prices[i]/weights[i]
		pricesPerKg.append((i, pricePerKg))

	pricesPerKg.sort(key=lambda tuple: tuple[1], reverse=True)

	solution = []
	totalWeight = 0
	for i, pricePerKg in pricesPerKg:
		if totalWeight + weights[i] <= capacity:
			totalWeight += weights[i]
			solution.append((i, weights[i]))
		elif totalWeight == capacity:
			break
		else:
			solution.append((i, capacity-totalWeight))
			break

	return solution