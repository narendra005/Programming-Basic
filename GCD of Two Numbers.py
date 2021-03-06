# Find GCD of Two Numbers
# GCD also known as HCF is highest common factor of 2 Numbers
# if there are no common number the function returns 0 
# Input is 2 Positive integers in any order
def gcd_find1(no1,no2):
    if(no1>no2): 
        no1,no2=no2,no1
    ## Check if Bigger no is divisible by smaller one 
    if(no2%no1==0):
        return no1
    else:
        m=no1//2
        flag=False
        while(m>=0):
            #print(m,no1%m,no2%m)
            if (no1%m==0 and no2%m==0):
                return m 
            m=m-1
        if flag==False:
            return 0

no1,no2=input().split()
no1=int(no1)
no2=int(no2)
gcd_find1(no1,no2)