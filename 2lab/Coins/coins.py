INFINITY = -1

def CoinChange(coins, target):
    solutions = {}
    return solveCoinChange(coins, target, solutions)


def solveCoinChange(coins, target, solutions):

    problem = target

    if problem in solutions.keys():
        return solutions[problem]

    if target in coins:
        solution = ([target],1) 
        solutions[problem] = solution
        return solution


    best_solution = ([], INFINITY)
    for coin in coins:
        new_target = target - coin

        solution = ([], INFINITY)
        if new_target > 0:

            (solution_coins, solution_number_of_coins) = solveCoinChange(coins, new_target, solutions)
            solution_coins = solution_coins[:]
            solution_coins.append(coin)
            solution_number_of_coins += 1
            solution = (solution_coins, solution_number_of_coins)

            if solution[1] < best_solution[1] or best_solution[1] == INFINITY:
                best_solution = solution

    solutions[problem] = best_solution
    return best_solution


if __name__ == "__main__":
    print(CoinChange([1, 5, 11], 26))
