import string

def caesarCipher(s: str, k):

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
    
    return r


n = int(input().strip())

s = input()

k = int(input().strip())

result = caesarCipher(s, k)

print(result)