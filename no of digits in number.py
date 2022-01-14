# Take Input of N Numbers and Print the Number of digit in it for 0 it would be 1 digit .
# digit here is the number of digit ie 1 2 or so on

def main(n):
    digit=0
    if n==0:
        return 1
    else:
        while(n>0):
            n=n//10
            digit=digit+1
    return digit

if __name__ == '__main__':
    N=int(input())
    max_digit=0
    l1=[]
    while(N>0):
        no=int(input())
        l1.append(main(no))
        #if ret>max_digit:
        #    max_digit=ret
        N=N-1
    #print(max_digit)
    for i in l1:
        print(i)