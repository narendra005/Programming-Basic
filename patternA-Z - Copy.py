# Given an integer N, print the corresponding pattern for N. For example if N = 4 then pattern will be like:
# Pattern Printing based on input
#A
#B B
#C C C
#D D D D

import pixiedust
N=int(input())
#for i in range(65,91,1):
#    alpha.append(chr(i))
for rows in range(1,N+1):
    for col in range (1,rows+1):
        if(rows==col):
            print(chr(rows+64),end="")
        else:         
            print(chr(rows+64),end=" ")
    print() 