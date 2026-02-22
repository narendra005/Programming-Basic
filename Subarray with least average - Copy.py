## Subarray with least average
# Given an array of size N, Find the subarray with least average of size k.
# Input A=[3, 7, 90, 20, 10, 50, 40] B=3
# output =3 
#Subarray between indexes 3 and 5 The subarray {20, 10, 50} has the least average  among all subarrays of size 3.


## Approach 1 
def solve(A,B):
    n=len(A)
    ps=[0]*n
    
    if B==1:  # Edge case to avoid multiple calculation in case if B=1 size of array is 1 so just find min value and its index is answer
        ix=min(A)
        ix=A.index(ix)
        return ix
    for i in range(n): # Array of Sum
        if i==0: ps[i]=A[i]
        else: ps[i]=ps[i-1]+A[i]

    ## Creating digit sum array of length B with ps arrya 

    j=-1
    ps1=[]  # ps1 is subarray of B element 
    ans=ix=0
    for i in range(B,len(ps)+1):
        if i==B:
            #print(ps[B+j],end=" ") 
            ps1.append(ps[B+j]) # This is for first iteration where 
            ix=i
            ans=ps[B+j]
        else:
            #print(ps[B+j] - ps[j],end=" ")
            temp=ps[B+j] - ps[j]
            ps1.append(temp)

            if temp<ans:
                ans=temp
                ix=i
        print(ps1)        
        j+=1

    return abs(ix-B)
	
	
## Apprach 2 , Here the Time complexity 0(N+B) mostly fails on number of B is very large. 

ans=sum(A[0:B])
temp=0
ix=0
for i in range(len(A)-B+1):
    temp=sum(A[i:B+i])
    print(temp,end=" ")
    if temp<ans:
        ans=temp
        ix=i
print("\n",ix)