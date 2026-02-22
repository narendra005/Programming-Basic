#Given a binary string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length of the longest consecutive 1’s that can be achieved.
#A = "111000" output is 3

class Solution:
    # @param A : string
    # @return an integer
    def solve(self,A):
        l = 0
        cnt = 0
        ans = 0
        for r in range(len(A)):
            cnt += A[r] == "0"
            if cnt > 1:
                cnt -= A[l] == "0"
                l += 1
            ans = max(ans, r - l + 1)
        return min(ans, A.count('1'))