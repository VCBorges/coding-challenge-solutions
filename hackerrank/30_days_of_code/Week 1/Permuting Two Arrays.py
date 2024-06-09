def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)

    cont = 0

    for i in range(len(A)):
        if A[i] + B[i] >= k:
            cont += 1
        else:
            print('NO')
            break

    if cont == len(A):
        print('YES')
