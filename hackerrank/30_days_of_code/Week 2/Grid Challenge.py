def gridChallenge(grid: list[str]) -> str:
    # 1. Sort the rows
    # 2. Check if all the columns are sorted in alphabetical order.
    for i in range(len(grid)):
        grid[i] = ''.join(sorted(grid[i]))

    result = 'YES'

    for j in range(len(grid[0])):
        column = [grid[k][j] for k in range(len(grid))]
        if ''.join(column) != ''.join(sorted(column)):
            result = 'NO'
            break

    return result
