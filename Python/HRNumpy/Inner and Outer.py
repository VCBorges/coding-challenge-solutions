import numpy as np
a = np.array([input().split()], int)
b = np.array([input().split()], int)
c = np.inner(a,b)
for i in c:
    print(i[0])
print(np.outer(a,b))

