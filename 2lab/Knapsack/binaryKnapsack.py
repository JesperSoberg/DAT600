def binaryKnapsack(weights, prices, capacity):
    indeces = [i for i in range(len(weights))]
    solutions = {}
    return solvebinaryKnapsack(indeces, weights, prices, capacity, solutions)


def solvebinaryKnapsack(indeces, weights, prices, capacity, solutions):

    problem = "".join([str(x) for x in indeces]) + f",{capacity}"
    if problem in solutions.keys():
        return solutions[problem]

    if len(indeces) == 1:
        index = indeces[0]
        if(weights[index] <= capacity):
            solution = (set(indeces), prices[index])
        else:
            solution = (set(), 0)

        solutions[problem] = solution
        return solution


    best_solution = (set(), 0)
    for i in indeces:
        temp_indeces = indeces[:]
        temp_indeces.remove(i)
        temp_capacity = capacity - weights[i]

        solution = (set(), 0)
        if temp_capacity >= 0:

            (solution_indeces, solution_price) = solvebinaryKnapsack(temp_indeces, weights, prices, temp_capacity, solutions)
            solution_indeces = solution_indeces.copy()
            solution_indeces.add(i)
            solution_price += prices[i]
            solution = (solution_indeces, solution_price)

        if solution[1] > best_solution[1]:
            best_solution = solution

    solutions[problem] = best_solution
    return best_solution


if __name__ == "__main__":
    #print(binaryKnapsack([10, 20, 30], [60, 100, 120], 50))
    print(binaryKnapsack([5, 15, 25,  50], [60, 50,  100, 120], 60))
