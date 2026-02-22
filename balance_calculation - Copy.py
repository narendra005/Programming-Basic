#Program to Take input of Balance of Bank then Add if input is 1 and amount in same line and 2 amount deduct 
#Balance - deduction in case the balance is insufficient print in Sufficient Balance
# calculation based upon 0 and 1 
# First first line is Balance Second is nof iteration


def main(Bal,itr):
    for i in range(itr,0,-1):
        no1=list(int(i) for i in input().split())
        i,ops=no1[0],no1[1]
        if i==1:
            Bal=Bal+ops
            print(Bal)
        elif i==2:
            if (Bal-ops<0):
                print("Insufficient Funds")
            else:
                Bal=Bal - ops
                print(Bal)
    
    return None

if __name__ == '__main__':
    Bal=int(input())
    itr=int(input())  
    main(Bal,itr)