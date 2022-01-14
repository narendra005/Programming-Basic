# Find How Many Sum of Numbers are there in A
# Input Array A and Second B is single Integer
# A=[1,2,3,2,1]
# B=5
sum=0
for i in range(len(A)):
    for j in range(1,len(A)):
        if(A[i]+A[j])==B:
            #print(A[i],A[j])
            sum=sum+1
sum=int(sum//2)
if B in A:
    sum=sum+1
print(sum)