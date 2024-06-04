import statistics


def findMedian(arr):
    return statistics.median(sorted(arr))


n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = findMedian(arr)

print(str(result) + '\n')
