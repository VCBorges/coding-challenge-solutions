import numpy as np
n = 2
la = []
lb = []
for ia in range(n):
    la1 = []
    arr1 = input('') 
    arr1 = arr1.split()
    for i in arr1:
        la1.append(int(i))
        if la1 not in la:
            la.append(la1)
a = np.array(la)
for ia in range(n):
    la1 = []
    arr1 = input('') 
    arr1 = arr1.split()
    for i in arr1:
        la1.append(int(i))
        if la1 not in lb:
            lb.append(la1)
b = np.array(lb)
print(np.dot(a,b))

#OUTRA RESPOSTA
'''n = int(input())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)
print(numpy.dot(a, b))'''