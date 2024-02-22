def printOptimalParens(solutions, i, j):
	if i == j:
		print(f'A{i}', end="")
	else:
		print("(", end="")
		printOptimalParens(solutions, i, solutions[i][j])
		printOptimalParens(solutions, solutions[i][j] + 1, j)
		print(")", end="")