# N-1 Pattern using Number
# input is Number
N=int(input())
j=N
for row in range(1,N+1):
    for col in range(1,j+1):
        if col==j:
            print(col,end="")
        else:
            print(col,end=" ")
    print()   
    j=j-1