#Given two integers A and B, find the greatest possible positive M, such that A % M = B % M.
# Difference of two number is the Modulus of it
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return (A-B if A>B else B-A)