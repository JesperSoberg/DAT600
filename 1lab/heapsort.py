import heapq

def heapsort(list):
    steps = 0
    result = []
    heapq.heapify(list)
    steps += len(list)
    for i in range(len(list)):
        result.append(heapq.heappop(list))
        steps += 1
    return result