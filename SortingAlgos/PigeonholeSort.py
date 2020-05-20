def PigeonholeSort(a):
    
        Min = min(a)
        Max = max(a)
        
        size = Max-Min+1
        
        holes = [0]*size
        
        for x in a:
            assert type(x) is int
            holes[x-Min] +=1
            
        i=0
        for count in range(size):
            while holes[count]>0:
                holes[count] -=1
                a[i] = count + Min
                i+=1
        
        return a