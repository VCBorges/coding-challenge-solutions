'''
Check if 2 strings share at least 1 equal character
'''

def twoStrings(s1: str, s2: str) -> str:
    for s in s1:
        if s in s2:
            return 'YES'
            
    return 'NO'