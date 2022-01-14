## Convert Binary to Decimal
# Input single digit 
def main(N):
    sum1=0
    i=0
    while(N>0):
        rem=N%10
        sum1=(2**i)*rem +sum1
        i=i+1
        N=N//10
    return sum1

if __name__ == '__main__':
    N=int(input())
    print(main(N))