def minion_game(string):
    vowel = 0
    conso = 0
    for i in range(len(string)):
        score = len(string) - i
        if string[i] in 'AEIOU':
            vowel+=score
        else:
            conso+=score
    if conso == vowel:
        print('Draw')
    if conso > vowel:
        print(f'Stuart {conso}')
    if conso < vowel:
        print(f'Kevin {vowel}')

s = "BANANA"
minion_game(s)