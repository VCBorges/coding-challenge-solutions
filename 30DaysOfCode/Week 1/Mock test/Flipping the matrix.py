def flippingMatrix(matrix):
    
    size = len(matrix)

    sorted_list = [j for i in matrix 
                        for j in i]

    b = []

    for i in range(size):
        b.append(max(sorted_list))
        sorted_list.remove(max(sorted_list))
        
    return (sum(b))


q = int(input().strip())

for q_itr in range(q):
    n = int(input().strip())

    matrix = []

    for _ in range(2 * n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = flippingMatrix(matrix)

    print(str(result) + '\n')
