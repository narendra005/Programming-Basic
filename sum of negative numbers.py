# Take input of N numbers and Print Sum of only Negative integers
# Input of N numbers and print sum of only negative numbers
# Input 1 is positive followed negative or positive integers
N=int(input())
sum=0
for i in range(N):
    no1=int(input())
    if no1<0:
        sum=sum+no1
print(sum)