def findZigZagSequence(a: list, n: int):
    a.sort() # [1, 2, 3, 4, 5]
    mid = int((n + 1)/2) # 3

    print(f'before a[mid]: {a[mid]}')
    print(f'before a[n-1]: {a[n-1]}')

    
    a[mid], a[n-1] = a[n-1], a[mid]

    print(f'after a[mid]: {a[mid]}')
    print(f'after a[n-1]: {a[n-1]}')
    
    print(f'after a: {a}')
    st = mid + 1
    ed = n - 1

    print(f'st: {st}')
    print(f'ed: {ed}')

    print(f'a[st]: {a[st]}')

    a[4], a[4] = a[4], a[4]
    
    print(f'a: {a}')
    
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed + 1

    # for i in range (n):
    #     if i == n-1:
    #         print(a[i])
    #     else:
    #         print(a[i], end = ' ')
    # return

a = [2,3,5,1,4]
n = len(a)
findZigZagSequence(a, n)