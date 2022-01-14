# Pattern No in revers
# Input is Number

N=int(input())
for row in range(1,N+1):
    for cols in range(1,row+1):
        if (cols==row):
            print(cols,end="")
        else:
            print(cols,end=" ")
    print()