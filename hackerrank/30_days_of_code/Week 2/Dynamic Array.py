def dynamicArray(n: int, queries: list[int]):
    arr = [[] for _ in range(n)]

    last_answer = 0
    answers = []

    for query in queries:
        idx = (query[1] ^ last_answer) % n

        if query[0] == 1:
            arr[idx].append(query[2])
        else:
            last_answer = arr[idx][query[2] % len(arr[idx])]
            answers.append(last_answer)
    return answers


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

q = int(first_multiple_input[1])

queries = []

for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))

result = dynamicArray(n, queries)

print('\n'.join(map(str, result)))
