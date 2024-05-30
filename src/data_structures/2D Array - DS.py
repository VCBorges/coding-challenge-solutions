def hourglassSum(arr: list[list[int]]) -> int:
    largest_sum = None
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            top = arr[i][j:j + 3]
            mid = arr[i + 1][j + 1]
            bot = arr[i + 2][j:j + 3]
            hourglass_sum = sum(top) + mid + sum(bot)
            if largest_sum is None:
                largest_sum = hourglass_sum
            elif hourglass_sum > largest_sum:
                largest_sum = hourglass_sum
    return largest_sum

arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

result = hourglassSum(arr)
