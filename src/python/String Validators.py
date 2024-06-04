from curses.ascii import isalnum, isalpha, isdigit, islower, isupper


def vali(string, method):
    return any(method(a) for a in string)


s = input()
print(vali(s, str.isalnum))
print(vali(s, str.isalpha))
print(vali(s, str.isdigit))
print(vali(s, str.islower))
print(vali(s, str.isupper))
