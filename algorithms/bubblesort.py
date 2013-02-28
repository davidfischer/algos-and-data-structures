def bubblesort(lst):
    for i in xrange(len(lst)):
        for j in xrange(1, len(lst)):
            if lst[j-1] > lst[j]:
                tmp = lst[j]
                lst[j] = lst[j-1]
                lst[j-1] = tmp
    return lst
