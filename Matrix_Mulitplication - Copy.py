# Problem Description
#You are given two integer matrices A(having M X N size) and B(having N X P). You have to multiply matrix A with B and return the resultant matrix. (i.e. return the matrix AB).

class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        n=len(A)
        m=len(B[0])
        p=len(B)
        ans=[[0]*m for _ in range(n)]
        for i in range(0,len(ans)):
            for j in range(0,len(ans[0])):
                for k in range(0,len(B)): # no of rows in B
                    ans[i][j]+=A[i][k]*B[k][j]
        return ans