# Get the factorial of Number using recursive fuction
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A==0:
            return
        else :
            ans= A * solve(A-1)
            return ans