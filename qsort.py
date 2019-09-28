def sort(a):
    # the base condition
    if a == []:
        return []
    # sort part
    else:
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        return [sort(left)] + [pivot] + [sort(right)]

def sorted(t):
    td = sort(t)
    return td[::2]
    print (td[::2])

def search(t,x):
    tt = sorted(t)
    x = input()
    if x in tt:
        print ("Ture")
    else:
        print ("Fals")

def insert(t,x):
    ti = sorted(t)
    x = input()
    ti.insert(x)
    return sort(t)
