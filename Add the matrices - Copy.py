#You are given two matrices A & B of same size, you have to return another matrix which is the sum of A and B.
#Input 1:
#A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
#B = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]
#Example Output
#Output 1:
#[[10, 10, 10], [10, 10, 10], [10, 10, 10]]

class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        n=len(A)
        m=len(A[0])
        ans=[[0]*m for _ in range(n)]
        # this creates n*m matrix with all zero to store the answer.
        if m==1:
            ans=[]
            for row in range(n):
                temp1=A[row][0]+B[row][0]
                ans.append([temp1])
            return ans
    
        for row in range(n):
            for col in range(m):
                ans[row][col]=(A[row][col]+B[row][col])
        return ans