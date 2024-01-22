import heapq
import math

def heapsort(list):
    n = len(list)
    steps = 0
    result = []
    heapq.heapify(list)
    steps += n * math.log(n, 2)
    for i in range(len(list)):
        result.append(heapq.heappop(list))
        steps += math.log(n, 2)
    return result