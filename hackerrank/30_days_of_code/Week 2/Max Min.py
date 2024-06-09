def maxMin(k, arr):
    arr.sort()
    # unf = []
    # for i in range(len(arr)-(k-1)):
    #     unf.append(arr[k+i-1]-arr[i])

    unf = [arr[k + i - 1] - arr[i] for i in range(len(arr) - (k - 1))]

    return min(unf)


n = int(input().strip())

k = int(input().strip())

arr = []

for _ in range(n):
    arr_item = int(input().strip())
    arr.append(arr_item)

result = maxMin(k, arr)

print(result)
