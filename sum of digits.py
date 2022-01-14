# Write a program to input T numbers(N) from user and print the sum of the digits of the given numbers.
# Input is integer of N Digits and outs sum of N 

N=int(input())

l1=[]
while(N>0):
    no=int(input())
    sum=0
    while(no>0):
        sum=no%10+sum
        no=no//10
    l1.append(sum)
    N=N-1
for i in l1:
    print(i,end=" ")