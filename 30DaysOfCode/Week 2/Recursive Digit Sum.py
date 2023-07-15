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
    p = str(sum(map(int, n)) * k)
    while len(p) > 1:
        p = str(sum(map(int, p)))
    return int(p)




first_multiple_input = input().rstrip().split()

n = first_multiple_input[0]

k = int(first_multiple_input[1])

result = superDigit(n, k)
