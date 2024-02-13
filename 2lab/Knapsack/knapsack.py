'''
n items
i th item worth vi kr and weighs wi kg
can carry at most W kg
'''
from FractionalKnapSack import solveFractionalKnapSack

def defineKnapsackProblem():
	weights = []
	prices = []
	print("Please type in the weight and price of the bags.")
	print('Press enter on empty input to leave.')
	while True:
		weight = input("What is the weight of the bag?: ")
		if weight == "":
			break
		price = input("What is the price of the bag?: ")
		if price == "":
			break
		weights.append(int(weight))
		prices.append(int(price))

	for idx, weight in enumerate(weights):
		print(f'Bag {idx}, weight {weight}, price {prices[idx]}')

	capacity = int(input("What is the bags capacity?: "))
	fraqSolution = solveFractionalKnapSack(weights, prices, capacity)
	print(fraqSolution)

if __name__ == "__main__":
	defineKnapsackProblem()
