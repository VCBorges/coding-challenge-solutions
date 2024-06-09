def pageCount(n, p):
    lista = list(range(n + 1))
    asc = p
    des = n - p
    output = [lista[i : i + 2] for i in range(0, len(lista), 2)]
    if asc > des:
        output = sorted(output, reverse=True)
    cont = -1
    for j in output:
        cont += 1
        print(j)
        if p in j:
            break
    return cont


n = int(input().strip())

p = int(input().strip())

result = pageCount(n, p)

print(str(result))
