#Print Star Pattern
# Only input is number of line positive integer.

N=int(input())
for i in range(1,N+1):
    for j in range(1,i+1):
        print("*",end="")
    print()