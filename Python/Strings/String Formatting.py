def print_formatted(number):
    for i in range(1,number+1):
        wt = len(bin(number)[2:])
        print(f'{str(i).rjust(wt)} {str(oct(i)[2:]).rjust(wt)} {str(hex(i)[2:]).rjust(wt)} {str(bin(i)[2:]).rjust(wt)}')

if __name__ == '__main__':
    #n = int(input())
    n = 17
    print_formatted(n)