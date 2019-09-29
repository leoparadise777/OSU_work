def sort(k,a):
    # the base condition
    if a == []:
        return []
    # sort part
    else:
        k = input()
        pivot = random.sample(a,1)
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        if k == len(left) + 1:
            return pivot
        elif k > len(left) + 1:
            k = k-1
            return sort(k,left)
        else:
            k = k-1
            return sort(k,right)