## Count AG in a String 
def solve(A):
    countA=countG=ans=0
    for i in range(len(A)):
        if A[i]=='A':
            countA+=1

        if A[i]=='G':
            ans=(ans+countA)
        print(i,A[i],countA,ans)
    return ans