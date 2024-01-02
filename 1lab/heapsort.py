import heapq

def heapsort(list):
    result = []
    heapq.heapify(list)
    for i in range(len(list)):
        result.append(heapq.heappop(list))
    return result