def minimumBribes(q: list):
    bribe = 0
    for i, n in enumerate(q): 
        pos = i + 1
        if n > pos:
            print(f'n: {n}, x: {pos}')
            dif = n - pos
            if dif >= 3:
                print('Too chaotic')
                # return
                    
            bribe += dif
            print(f'n: {n}, dif: {dif}')
    
    print(bribe)


# q = list(map(int,'2 1 5 3 4'.split(' ')))
# q = list(map(int,'2 5 1 3 4'.split(' ')))
q = list(map(int,'1 2 5 3 7 8 6 4'.split(' ')))

'1 2 5 3 7 8 4 6'

minimumBribes(q)


# t = int(input().strip())

# for t_itr in range(t):
#     n = int(input().strip())

#     q = list(map(int, input().rstrip().split()))

    # minimumBribes(q)
