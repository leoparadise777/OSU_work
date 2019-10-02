import random

def qselect(k,a):
    if len(a) >0:
        i=random.randint(0, len(a)-1)
        a[0],a[i]=a[i],a[o]
        pivot=a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]

        #a = left + [pivot] + right
        if k == len(left) + 1:
            return pivot
        elif k < len(left) + 1:

            return qselect(k, left)
        else:
            return qselect(k-len(left)-1, right)


print(qselect(4, [3,7,6,9,1,8,10,4]))
