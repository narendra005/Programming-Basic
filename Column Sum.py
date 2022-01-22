#You are given a 2D integer matrix A, return a 1D integer vector containing column-wise sums of original matrix.
# Input 1:
#[1,2,3,4]
#[5,6,7,8]
#[9,2,3,4]
#Example Output
#Output 1:{15,10,13,16}

class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        n=len(A)
        m=len(A[0])
        ans=[]
        for col in range(m):
            sum1=0
            for row in range(n):
                sum1=A[row][col]+sum1
            ans.append(sum1)
        return ans