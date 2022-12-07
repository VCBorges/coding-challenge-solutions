def pangrams(s):
    # Write your code here
    s = s.lower()
    a = s.replace(' ','')
    unico = set()
    for i in a:
        unico.add(i)
    if len(unico) == 26:
        return 'pangram'
    else:
        return 'not pangram'


