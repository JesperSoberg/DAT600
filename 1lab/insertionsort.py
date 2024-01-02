def insertionsort(list):
    for i, element in enumerate(list):
        if i == 0:
            continue

        if element < list[i-1]:
            h = i-1

            while list[h] > list[i]:
                list[i] = list[h]
                list[h] = element

                if h == 0:
                    break

                h -= 1
                i -= 1
    return list