#To change the Number Sequence 4321 becomes 1234
# Positive Input Integer 
# Program Can be enchanced to cater negative numbers
# Constraints Works with Positive Numbers only
n=int(input())  # Take Input of number 
ans=0  # Temp Variable to Store Anser 
while(n>0):
    rem=n%10
    ans=(ans * 10) + rem
    #print(ans,rem,n)
    n=n//10
print(ans)