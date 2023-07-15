# WORKS
# def superDigit(n: str, k: int) -> int:
#     arr = list(int(x) for x in n)
#     p = str(sum(arr) * k)
         
#     while len(p) > 1:
#         arr = list(int(x) for x in p)
#         p = str(sum(arr))
            
#     super_digit = int(p)
#     return super_digit


def superDigit(n: str, k: int) -> int:
    p = sum(map(int, n)) * k
    while p > 9:
        p = sum(map(int, str(p)))
    return p




first_multiple_input = input().rstrip().split()

n = first_multiple_input[0]

k = int(first_multiple_input[1])

result = superDigit(n, k)
