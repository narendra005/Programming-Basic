#You are given a 2D integer matrix A, return a 1D integer vector containing row-wise sums of original matrix.
# Input 1:
#[1,2,3,4]
#[5,6,7,8]
#[9,2,3,4]
#Example Output
#Output 1: {10,26,18}

class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        n=len(A)
        m=len(A[0])
        ans=[]
        for row in A:
            ans.append(sum(row))
        return ans