a,b = map(int, input().split())
for i in range(0,int((a-1)/2)):
    print('-'*((int((b-3)/2))-(3*i))+'.|.'*(1+(i*2))+'-'*((int((b-3)/2))-(3*i)))
print(f'-'*(int((b - 7) / 2))+'WELCOME'+'-'*(int((b - 7) / 2)))
for i2 in range((int((a-1)/2))-1,-1,-1):
    print('-'*((int((b-3)/2))-(3*i2))+'.|.'*(1+(i2*2))+'-'*((int((b-3)/2))-(3*i2)))