def reverseArray(a: list[int]):
    return [a[-i] for i in range(1, len(a) + 1)]


arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))

res = reverseArray(arr)
