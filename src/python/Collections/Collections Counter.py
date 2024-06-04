list_shoe_size = []
coust = 0
number = []
price = []

number_shoes = int(input())
list_shoes = input().split()
for number_shoe in range(len(list_shoes)):
    list_shoes[number_shoe] = int(list_shoes[number_shoe])

customers = int(input())
for i in range(customers):
    shoe_size = input().split()
    list_shoe_size.append(shoe_size)

for i3 in range(len(list_shoe_size)):
    list_shoe_size[i3] = list(map(int, list_shoe_size[i3]))

for i4 in list_shoe_size:
    price.append(i4[1])
    number.append(i4[0])

for i5 in range(len(number)):
    if number[i5] in list_shoes:
        list_shoes.remove(number[i5])
        coust += price[i5]

print(price)

"""import collections

numShoes = int(input())
shoes = collections.Counter(map(int, input().split()))
numCust = int(input())

income = 0

for i in range(numCust):
    size, price = map(int, input().split())
    if shoes[size]: 
        income += price
        shoes[size] -= 1

print(income)"""
