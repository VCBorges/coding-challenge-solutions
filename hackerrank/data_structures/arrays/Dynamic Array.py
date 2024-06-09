def dynamicArray(n: int, queries: list[int]) -> list[int]:
    last_answer = 0
    arrs = [[] for _ in range(n)]
    answers = []
    t = 0
    for i in range(len(queries)):
        x = queries[i][1]
        y = queries[i][2]
        if queries[i][0] == 1:
            idx = (x ^ last_answer) % n
            arrs[idx].append(y)
            t += 1
        else:
            idx = (x ^ last_answer) % n
            last_answer = arrs[idx][y % len(arrs[idx])]
            answers.append(last_answer)

    return answers


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

q = int(first_multiple_input[1])

queries = []

for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))

result = dynamicArray(n, queries)
