#Take input of Number and Print Series in below format
# 1
# 1 2
# 1 2 3 
# Just pattern printing exercise
# input is one positive integer
N=int(input())
for row in range(1,N+1):
    for cols in range(1,row+1):
        print(cols,end=" ")
    print()
