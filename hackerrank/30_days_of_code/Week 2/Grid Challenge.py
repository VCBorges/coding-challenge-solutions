def gridChallenge(grid: list) -> str:
    columns = [[] for _ in range(len(grid))]

    for i, row in enumerate(grid):
        grid[i] = ''.join(sorted(row))
        for j, letter in enumerate(grid[i]):
            columns[j].append(letter)

    result = 'YES'
    for column in columns:
        if column != sorted(column):
            result = 'NO'
            break

    return result


t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = gridChallenge(grid)

    print(result)
