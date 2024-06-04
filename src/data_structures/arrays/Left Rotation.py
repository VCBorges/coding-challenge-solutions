def rotateLeft(d: int, arr: list[int]) -> list[int]:
    output = [None for _ in range(len(arr))]
    for i in range(len(arr)):
        output[i - d] = arr[i]
    return output


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

d = int(first_multiple_input[1])

arr = list(map(int, input().rstrip().split()))

result = rotateLeft(d, arr)