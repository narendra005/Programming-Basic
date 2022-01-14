# You are given an integer A in decimal (base 10).
# Return a string denoting the binary (base 2) form of the integer A.
def BinaryToDecimal(n):
    ans=0
    p=1
    while(n>0):
        rem=n%2
        ans=ans+rem*p
        p=p*10
        n=n//2
    return ans