#Given an integer array A of size N. In one second you can increase the value of one element by 1.
#Find the minimum time in seconds to make all elements of the array equal.
# A = [2, 4, 1, 3, 2]
# output 8
# We can change the array A = [4, 4, 4, 4, 4]. The time required will be 8 seconds.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max1=max(A)
        count1=0
        for i in range(len(A)):
            count1=max1 -A[i]+count1
        return count1
