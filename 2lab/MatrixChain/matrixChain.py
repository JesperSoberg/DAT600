from printOptimalParens import printOptimalParens

INFINITY = 999999999999999999

def matrixChainOrder(dimensions):
    matrices = len(dimensions) - 1
    multiplications = []
    solutions = []
    for i in range(matrices):
        multiplications.append([0]*matrices)
        solutions.append([None]*matrices)
    for length in range(2,matrices+1):
        for i in range(matrices-length+1):
            j = i + length -1
            multiplications[i][j] = INFINITY
            for kut in range(i, j):
                operations = multiplications[i][kut] + multiplications[kut+1][j] + dimensions[i] * dimensions[kut+1] * dimensions[j+1]
                if operations < multiplications[i][j]:
                    multiplications[i][j] = operations
                    solutions[i][j] = kut

    return multiplications, solutions


if __name__ == "__main__":
    (m, s) = matrixChainOrder([30,35,15,5,10,20,25])
    printOptimalParens(s, 0, len(s)-1)


