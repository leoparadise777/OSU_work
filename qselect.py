from random import randint

def qselect(i, a):
    if len(a) > 0:
        i = randint(0, len(a)-1)
        a[0], a[i] = a[i], a[0]
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        a = left + [pivot] + right
        if i == len(left) + 1:
            return pivot
        elif i > len(left) + 1:
            return qselect(i-len(left)+1, right)
        else:
            return qselect(i, left)


#print(qselect(4 ,[3,7,6,9,1,8,10,4]))
