s = 'abacbcbca'
t = 'beca'

test = set()
result = 0

for i in t:
    if i in s:
        c = s.count(i)
        test.add(c)
        for j in test:
            result = j
        if result > 1:
            break
    else:
        result = 0 
        break

print(result)
