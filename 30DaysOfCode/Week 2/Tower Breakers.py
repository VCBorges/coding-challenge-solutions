
def towerBreakers(n, m):
    return 2 if n % 2 == 0 or m == 1 else 1

t = int(input().strip())

for t_itr in range(t):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = towerBreakers(n, m)

    print(str(result))    