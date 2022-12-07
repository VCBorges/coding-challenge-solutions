import re
s = "BANANA"
cp = 0
vp = 0
vowel = []
conso = []

for i in range(len(s)):
    if s[i] in "AEIOU":
        sv = s[i:]  #ANANA
        for l in range(len(sv)): 
            sg = sv[:l+1] #sg = A
            if sg not in vowel:
                vowel.append(sg)
                count_string = len(re.findall(sg,sv))
                vp += count_string
                print(f'{sg} - {count_string}')
            
    elif s[i] not in "AEIOU":
        sv = s[i:]  #ANANA
        for l in range(len(sv)): 
            sg = sv[:l+1] #sg = A
            if sg not in conso:
                conso.append(sg)
                count_string = len(re.findall(sg,sv))
                cp += count_string
                print(f'{sg} - {count_string}')
    
print(f'VOGAL {vp} ----- CONSOANTE {cp}')
