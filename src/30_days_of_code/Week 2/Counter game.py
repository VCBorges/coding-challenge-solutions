import math


def is_power_of_2(number: int) -> bool:
    if number % 2 == 0:
        return number > 0 and (number & (number - 1)) == 0
    return False



def get_closest_lower_power_of_2(number: int) -> int:
    if number <= 0:
        return 0 
    
    power = int(math.log2(number))
    closest_power = 2 ** power
    return closest_power
    
    

def counterGame(n: int):
    count = 0
    while n > 1:
        if is_power_of_2(n):
            n = int(n / 2)
        else:
            n -= get_closest_lower_power_of_2(n)
        count += 1
    return 'Richard' if count % 2 == 0 else 'Louise'



t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())

    result = counterGame(n)
    print(result)
