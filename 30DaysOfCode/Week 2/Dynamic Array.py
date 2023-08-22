def dynamicArray(n: int, queries: list[int]):
    arr = [
        [] for _ in range(n)
    ]
    
    last_answer = 0
    result = []
    
    for query in queries:
        if query[0] == 1:
            idx = ((query[1] ^ last_answer) % n)
            arr[idx].append(query[2])
        else:
            idx = ((query[1] ^ last_answer) % n)
            # print(f'last answer {last_answer}')
            last_answer = idx
            # result.append(last_answer)
        # print(idx)
    
    
    
    print(result)
    print(f'arr {arr}')
    
    return arr


# first_multiple_input = input().rstrip().split()

# n = int(first_multiple_input[0])

# q = int(first_multiple_input[1])

# queries = []

# for _ in range(q):
#     queries.append(list(map(int, input().rstrip().split())))


# print(f'queries {queries}')    

n = 2

queries = [
    [1, 0, 5],
    [1, 1, 7],
    [1, 0, 3],
    [2, 1, 0],
    [2, 1, 1],
]

result = dynamicArray(n, queries)

print(result)