def strings_xor(s, t):
    res = ''
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0'
        else:
            res += '1'

    return res


s = input()
t = input()

print(strings_xor(s, t))

# def teste():
#     s = input()
#     t = input()
#     print(''.join('0' if s[i] == t[i] else '1' for i in range(len(s))))
