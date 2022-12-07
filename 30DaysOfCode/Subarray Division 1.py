n = 5
s = [2,2,1,3,2]

d = 4
m = 2

for i in s:
    sc = s.copy()
    sc.remove(i)

    print('-=' * 20)
    for j in sc:
        print(f'{i} + {j} = {i+j}')
        if i + j == 4:
            s.remove(i)
            s.remove(j)
            break
            