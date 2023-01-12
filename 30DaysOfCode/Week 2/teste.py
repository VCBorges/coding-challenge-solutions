lista = list(range(8))

p = 4

asc = p

des = n - p

print(des)

output = [lista[i:i + 2] for i in range(0, len(lista), 2)]


if asc > des:
    output = sorted(output, reverse=True)

print(output)
cont = -1

for j in output:
    cont += 1
    print(j)
    if p in j:
        break
print(cont)

# sorted(output, reverse=True)