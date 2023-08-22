

def sumXor(n):
    cont = 0
    for x in range(n + 1):
        if n + x is n ^ x:
            cont += 1
        
    return cont



# n = int(input().strip())

n = 1099511627776

result = sumXor(n)

print(result)