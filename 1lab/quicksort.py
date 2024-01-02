def quicksort(list):
    if len(list) > 1:
        pivot = list[0]

        front = 1
        back = len(list)-1

        left = []
        right = []

        while front < back:
            while list[front] <= pivot and front < back:
                left.append(list[front])
                front += 1
            while list[back] > pivot and back > front:
                right.append(list[back])
                back -= 1
            if front < back:
                left.append(list[back])
                right.append(list[front])
                front += 1
                back -= 1
        
        if list[back] <= pivot:
            left.append(list[back])
        else:
            right.append(list[back])

        left.append(pivot)
        
        left = quicksort(left)
        right = quicksort(right)
        
        return left + right
    return list