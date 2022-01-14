# Magic Numbers is number which is 5 or power . Need to find Nth Magic Number
#5 25 30 125 130 150 155 625 630 650
def magic_number(n):
    pow = 5
    ans = 0
    while(n>0):
        rem=n%2
        ans=ans+rem*pow
        pow=pow*5
        n=n//2
        print(rem,ans,pow,n)
    return ans