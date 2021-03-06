def merge(array, left, mid, right): 

    leftLength, rightLength = mid - left + 1, right - mid 
    Left, Right = [], [] 
    for i in range(0, leftLength): 
        Left.append(array[left + i]) 
    for i in range(0, rightLength): 
        Right.append(array[mid + 1 + i]) 
	
    i, j, k = 0, 0, left 

    while i < leftLength and j < rightLength: 
	
        if Left[i] <= Right[j]: 
            array[k] = Left[i] 
            i += 1
		
        else: 
            array[k] = Right[j] 
            j += 1
		
        k += 1
	
    while i < leftLength: 
	
        array[k] = Left[i] 
        k += 1
        i += 1
	
    while j < rightLength: 
        array[k] = Right[j] 
        k += 1
        j += 1


def insertionSort(array, left, right): 

    for i in range(left + 1, right+1): 
	
        temp = array[i] 
        j = i - 1
        while array[j] > temp and j >= left: 
		
            array[j+1] = array[j] 
            j -= 1
		
        array[j+1] = temp
	

def TimSort(array, n): 
    Limit=32 
    for i in range(0, n, Limit): 
        insertionSort(array, i, min((i+31), (n-1))) 
    size = Limit 
    while size < n: 
	
        for left in range(0, n, 2*size): 
		 
            mid = left + size - 1
            right = min((left + 2*size - 1), (n-1)) 
	
            merge(array, left, mid, right) 
		
        size = 2*size 
    
    return array
