from itertools import product

A = []
B = []
a = input().split()
for i in a:
    A.append(int(i))
b = input().split()
for i2 in b:
    B.append(int(i2))
print(*list(product(A, B, repeat=1)))


"""A = input().split()
A = list(map(int,A))
B = input().split()
B = list(map(int, B))
output = list(product(A,B))
for i in output:
    print(i, end = " ");"""
