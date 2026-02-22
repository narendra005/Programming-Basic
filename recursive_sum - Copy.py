# sum of even number using recursive function
def sum_even(N):
    if N==0:
        return 
    else:
        if N%2==0:
            print(N)
            sum_even(N-1)
        return 
    
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        return sum_even(A);
