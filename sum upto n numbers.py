# Take Input of Number and print the sum from 1--n for 2 sum would be 1+2 for 3 it 1+2+3
# Input is positive integer
# output is sum e.g for 2 sum 1+2 =3 for 5 sum would be 1+2+3+4+5
no1=int(input())
sum=0
while(no1>0):
    sum=sum+no1
    no1=no1-1
print(sum)