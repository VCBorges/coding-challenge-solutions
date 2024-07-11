def marcsCakewalk(calorie: list[int]) -> int:
    calorie.sort(reverse=True)
    calorie_count = 0
    for i in range(len(calorie)):
        calorie_count += ((2 ** i) * calorie[i])
    return calorie_count

if __name__ == '__main__':
    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))
    
    calorie = [5, 10, 7]

    result = marcsCakewalk(calorie)