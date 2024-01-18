def quicksort(liste, start, slutt):
    if start < slutt:
        midt = partition(liste, start, slutt)
        quicksort(liste, start, midt-1)
        quicksort(liste, midt+1, slutt)
    return liste


def partition(liste, start, slutt):
    pivot = liste[slutt]
    i = start-1
    for j in range(start, slutt):
        if liste[j] <= pivot:
            i += 1
            liste[i], liste[j] = liste[j], liste[i]
    liste[i+1], liste[slutt] = liste[slutt], liste[i+1]
    return i+1