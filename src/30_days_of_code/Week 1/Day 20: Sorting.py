#conta quantos "swaps" foram feitos em uma lista até que ela esteja ordenada
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
nofswap = 0
for i in range(0,n-1):
    for i in range(0,n-1):
        if a[i]>a[i+1]:
            a[i],a[i+1] = a[i+1],a[i] # é possivel alterar o elementos de uma lista, até mais que um por vez
            nofswap +=1

print("Array is sorted in", nofswap, "swaps.")
print("First Element:",a[0])
print("Last Element:",a[-1])
