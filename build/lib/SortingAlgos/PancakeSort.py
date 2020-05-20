
def flip(arr, i):                    
    start = 0
    while start < i:
        temp = arr[start]
        arr[start] = arr[i]
        arr[i] = temp
        start = start + 1
        i = i - 1


def findMax(arr, n):                    
    maxi = 0
    for i in range(0,n):
        if arr[i] > arr[maxi]:
            maxi = i
    return maxi


def pancakeSort(arr, n):               
    curr_size = n
    while curr_size > 1:
        maxi = findMax(arr, curr_size)
        if maxi != curr_size-1:
            flip(arr, maxi)
            flip(arr, curr_size-1)
        curr_size -= 1

    return arr

