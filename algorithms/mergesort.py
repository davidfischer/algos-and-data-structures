def mergesort(lst):
    if len(lst) <= 1:
        return lst

    middle = int(len(lst) / 2)
    left = mergesort(lst[:middle])
    right = mergesort(lst[middle:])

    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result + left[i:] + right[j:]
