def sockMerchant(n, ar):
    set_ar = set(ar)

    cont = 0

    for i in set_ar:
        qnt = ar.count(i)
        if qnt >= 2:
            if qnt % 2 == 0:
                cont += qnt / 2
                print(i, qnt, cont)
            else:
                cont += int(qnt / 2)
                
    return int(cont)

n = int(input().strip())

ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)

print(str(result))

