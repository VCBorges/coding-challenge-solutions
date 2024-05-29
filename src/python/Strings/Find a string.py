def count_substring(string, sub_string):
    cont = 0 
    for i in range(0,len(string)):
        if string[i:].startswith(sub_string): #checka se string[começo:até o final] começa com sub_string
            cont+=1
    return cont

if __name__ == '__main__':
    string = 'ABCDCDC'
    sub_string = 'CDC'
    
    count = count_substring(string, sub_string)
    print(count)