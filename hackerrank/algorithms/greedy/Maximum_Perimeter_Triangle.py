from rich import print

def maximum_perimeter_triangle(sticks: list[int]) -> list[int]:
    maximum_perimeter_trinagle = None
    max_perimeter = 0
    lenght = len(sticks)
    for i in range(lenght):
        for j in range(i + 1, lenght):
            for k in range(j + 1, lenght):
                if ( 
                    sticks[i] + sticks[j] > sticks[k]
                    and sticks[i] + sticks[k] > sticks[j]
                    and sticks[k] + sticks[j] > sticks[i]
                ):
                    perimeter = sticks[i] + sticks[j] + sticks[k]
                    if perimeter > max_perimeter:
                        max_perimeter = perimeter
                        triangle = [sticks[i], sticks[j], sticks[k]]
                        triangle.sort()
                        maximum_perimeter_trinagle = triangle
                        
    if not maximum_perimeter_trinagle: 
        return [- 1]
    
    return maximum_perimeter_trinagle

def maximum_perimeter_triangle(sticks:list[int]) -> list[int]:
    sticks.sort()
    n = len(sticks)
    
    for i in range(n - 3, -1, -1):
        if sticks[i] + sticks[i + 1] > sticks[i + 2]:
            return [sticks[i], sticks[i + 1], sticks[i + 2]]
    
    return [-1]
    

if __name__ == '__main__':
    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximum_perimeter_triangle(sticks)
    print(f'{result = }')