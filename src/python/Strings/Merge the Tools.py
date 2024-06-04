import re


def merge_the_tools(string, k):
    a = re.findall('.' * k, string)
    lista = []
    for item in a:  # item = string
        b = item.split()  # b = lista
        lista.append(b)
    a = lista
    b = []
    for i in a:
        c = []
        for i2 in i:
            for i3 in i2:
                if i3 not in c:
                    c.append(i3)
                    if c not in b:
                        b.append(c)
    for i4 in b:
        print(''.join(str(x) for x in i4))


if __name__ == '__main__':
    string, k = 'AABCAAADAdsfdsfgfdfgdfsg', 3
    merge_the_tools(string, k)
