def quicksort(l):
    if l == []:
        return l

    lesser = []
    greater = []
    for e in l[1:]:
        if e < l[0]:
            lesser.append(e)
        else:
            greater.append(e)

    return quicksort(lesser) + [l[0]] + quicksort(greater)
