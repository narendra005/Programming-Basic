# Print different Number Pattern
for i in range(1,N+1):
    for j in range(1,N-i+1):
        print('0',end=' ')
    for j in range(i,2*i):
        print(j,end=' ')
    for j in range(2*i-1,i,-1):
        print(j-1,end=' ')
    for j in range(i+1,N+1):
        print('0',end=' ')    
    print() 