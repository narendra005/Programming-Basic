#Given a number A in the form of string. Check if the number is divisible by 8 or not.
#Return 1 if it is divisible by 8 else return 0.
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n=len(A)-1
        A[n-2::] # The array will give last 3 digit if divisible the number is divisible by 8
        return(1 if int(A)%8==0 else 0)