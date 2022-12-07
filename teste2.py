import re
string, k = 'AABCAAADAaaa', 3
a = re.findall("."*k,string)
lista = []
for item in a: #item = string
    b = item.split() #b = lista
    lista.append(b)
print(lista)
