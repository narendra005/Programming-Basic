def repeatedNumber(A):
    max1=A[0]
    count1=0
    ans=[]
    n=len(A)//3
    for i in range(0,len(A)):
        count1=1
        for j in range(i+1,len(A)):
            if A[i]==A[j]: 
                count1+=1
        if count1>n:
            ans.append(A[i])
               
    return ans
A =[ 1, 1, 1, 2, 3,1,5,7 ]
repeatedNumber(A)
