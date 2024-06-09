from rich import print

# def func(arr: list[int]):


def arrayManipulation(n: int, queries: list[list[int]]) -> int:
    arr = [0 for _ in range(n + 1)]

    # Apply the difference array concept
    for query in queries:
        a, b, k = query
        arr[a - 1] += k
        if b < n:
            arr[b] -= k

    # print(f'{arr = }')
    # Calculate the prefix sum and find the maximum value
    max_value = 0
    current_value = 0
    for i in range(n):
        current_value += arr[i]
        print(f'{current_value = }')
        if current_value > max_value:
            max_value = current_value

    return max_value


if __name__ == '__main__':
    # first_multiple_input = input().rstrip().split()

    first_multiple_input = '53'

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = [
        [1, 5, 3],
        [4, 8, 7],
        [6, 9, 1],
    ]

    # queries = []

    # for _ in range(m):
    #     queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(f'{result = }')
