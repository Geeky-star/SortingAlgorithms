
def getNextGap(gap):
    
    gap = (gap*10)//13
    if gap<1:
        return 1
    return gap


def CombSort(a):
    n = len(a)
    
    gap = n
    swapped = True
    
    while gap !=1 or swapped == 1:
        gap = getNextGap(gap)
        swapped = False
        
        for i in range(0,n-gap):
            if a[i] > a[i+gap]:
                a[i],a[i+gap] = a[i+gap],a[i]
                swapped = True
    
    return a         

