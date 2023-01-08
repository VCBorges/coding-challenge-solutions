import math

n = 20

ar = [4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5]

# n = 9

# ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

ar2 = set(ar)

cont = 0

for i in ar2:
    qnt = ar.count(i)
    if qnt >= 2:
        if qnt % 2 == 0:
            cont += qnt / 2
            print(i, qnt, cont)
        else:
            cont += int(qnt / 2)


            
            
print(cont)
        