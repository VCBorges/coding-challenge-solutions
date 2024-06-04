def bomberMan(n, grid):
    # Write your code here
    for i in range(len(grid)):
        pixel = grid[i]
        print(pixel)
        for j in range(len(pixel)):
            print(pixel[j])
    return grid


first_multiple_input = '6 7 3'.split(' ')

r = int(first_multiple_input[0])

c = int(first_multiple_input[1])

n = int(first_multiple_input[2])

# grid = []

# for _ in range(r):
#     grid_item = input()
#     grid.append(grid_item)

grid = ['.......', '...O...', '....O..', '...O...', '.......', 'OO.....', 'OO.....']

result = bomberMan(n, grid)


print(result)
