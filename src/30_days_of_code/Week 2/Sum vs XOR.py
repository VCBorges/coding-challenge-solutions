
def sumXor(n):
    # cont = 0
    # for x in range(n + 1):
    #     if n + x is n ^ x:
    #         cont += 1
        
    # return cont
    unset_bits = bin(n).count('0') - 1 if n > 0 else 0
    return 2**unset_bits


# n = int(input().strip())

n = 5

result = sumXor(n)

print(result)