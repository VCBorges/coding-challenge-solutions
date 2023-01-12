def findZigZagSequence(a, n):
    
    a.sort() #? a = [1,2,3,4,5]
    
    #? a[0] = 1
    #? a[1] = 2
    #? a[2] = 3
    #? a[3] = 4
    #? a[4] = 5
    
    
    mid = int((n + 1)/2) #? mid = 3
    
    #? a[3] == 4, a[4] == 5 = a[4] == 5, a[3] == 4
    a[mid], a[n-1] = a[n-1], a[mid] 
    
    # ? a = [1, 2, 3, 5, 4]

    #? st = 4
    st = mid + 1
    
    #? ed = 4
    ed = n - 1
    
    #? while 4 <= 4:
    while(st <= ed):
        
       #? a[4] == 4, a[4] == 4 = a[4] == 4, a[4] == 4
        a[4], a[4] = a[4], a[4]
        st = st + 1
        ed = ed + 1

    
    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return 

test_cases = 1
for cs in range (test_cases):
    n = 5
    a = [2,3,5,1,4]
    findZigZagSequence(a, n)

    print(findZigZagSequence(a, n))

