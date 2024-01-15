def mergesort(list):
    steps = 0
    if len(list) > 1:
        half = len(list)//2
        left = list[:half]
        right = list[half:]

        steps += 3

        steps += mergesort(left)
        steps += mergesort(right)

        i=j=k=0

        steps += 1

        while j < len(left) and k < len(right):
            if left[j] < right[k]:
                list[i] = left[j]
                j += 1
                steps += 2
            else:
                list[i] = right[k]
                k += 1
                steps += 2
            i += 1
            steps += 1

        while j < len(left):
            list[i] = left[j]
            i += 1
            j += 1
            steps += 3

        while k < len(right):
            list[i] = right[k]
            i += 1
            k += 1
            steps += 3
    
    return steps

