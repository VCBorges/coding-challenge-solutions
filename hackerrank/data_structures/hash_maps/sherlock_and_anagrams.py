'''
Calculate  how many  
'''

def sherlockAndAnagrams(s: str) -> str:
    d = {}
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_string = ''.join(sorted(s[i : j + 1]))
            d.setdefault(sub_string, 0)
            d[sub_string] += 1

    anagrams = 0
    for key in d:
        anagrams += int(((d[key] - 1) * d[key]) / 2)

    return anagrams
