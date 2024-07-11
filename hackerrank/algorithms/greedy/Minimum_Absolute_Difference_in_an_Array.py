def minimumAbsoluteDifference(arr: list[int]) -> int:
    arr.sort()
    min_abs_diff = 10**20
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        min_abs_diff = min(diff, min_abs_diff)
    return min_abs_diff
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    
    result = minimumAbsoluteDifference(arr)