# prime factor of number
# PrimeFactor(100) will give all prime factor
def PrimeFactor(n):
    i=2
    while i*i<=n:
        if n%i==0:
            while n%i==0:
                print(i,end=",")
                n=n//i
        i=i+1