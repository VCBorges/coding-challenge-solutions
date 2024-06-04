def birthday(s, d, m):
    j = m
    i = 0
    count = 0

    while j <= len(s):
        if sum(s[i:j]) == d:
            print(f'{s[i:j]}')
            count += 1

        i += 1
        j += 1

    return count
