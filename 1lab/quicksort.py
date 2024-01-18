def quicksort(liste, start, slutt):
    steg = 0
    if start < slutt:
        midt, partition_steg = partition(liste, start, slutt)
        steg += partition_steg
        steg += quicksort(liste, start, midt-1)
        steg += quicksort(liste, midt+1, slutt)
    return steg


def partition(liste, start, slutt):
    steg = 0
    pivot = liste[slutt]
    i = start-1
    steg += 2
    for j in range(start, slutt):
        if liste[j] <= pivot:
            i += 1
            liste[i], liste[j] = liste[j], liste[i]
            steg += 2
        steg += 1
    liste[i+1], liste[slutt] = liste[slutt], liste[i+1]
    steg += 1
    return i+1, steg