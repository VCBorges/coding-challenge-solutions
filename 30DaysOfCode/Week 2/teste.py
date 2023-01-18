import string

alphabet = string.ascii_lowercase

i = 26

while i > 25:
    i = i - 25 - 1

s = 'middle-Outz'

k = 2

r = ''
for i in s:
    if i.isalpha():
        # print(i)
        if i.isupper():
            alphabet = string.ascii_uppercase
        elif i.islower():
            alphabet = string.ascii_lowercase
        p = alphabet.index(i)

        while p + k > 25:
            p = p - 25 - 1
                
        r += alphabet[p + k]
        print(r)
    else:
        r += i
print(r)
