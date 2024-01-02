def mergesort(list):
    if len(list) > 1:
        half = len(list)//2
        left = list[:half]
        right = list[half:]

        mergesort(left)
        mergesort(right)

        i=j=k=0

        while j < len(left) and k < len(right):
            if left[j] < right[k]:
                list[i] = left[j]
                j += 1
            else:
                list[i] = right[k]
                k += 1
            i += 1

        while j < len(left):
            list[i] = left[j]
            i += 1
            j += 1

        while k < len(right):
            list[i] = right[k]
            i += 1
            k += 1
    
    return list

