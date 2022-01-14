# The program finds prime number in range
# Input is 2 positive integer in single line seperated by comma
# Logic : Factors of numbers small and big if i*i becomes greater than Number
# Assumption no2 is greater then no1
# Here to Simplify there are two Program one to find the range second just to fine if number is prime or no
def isPrime(no):
    i=2
    while(i*i<=no):
        if no%i==0: 
            return False
        if i*i>no:
            return False 
        i+=1
    return True
    
def printPrime(a,b):
    for i in range(a,b+1):
        if isPrime(i):
            print(i,end=" ")

no1,no2=input().split()
no1=int(no1)
no2=int(no2)
printPrime(no1,no2)