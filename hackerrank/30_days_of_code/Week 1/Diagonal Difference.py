def diagonalDifference(arr):
    lenght = len(arr)
    soma = 0
    soma_i = 0
    for i in range(lenght):
        s = arr[i][i]
        soma += s

        n = arr[i][(lenght - 1) - i]
        soma_i += n

    return abs(soma + soma_i)


n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)


print(diagonalDifference(result))

print(len())
