#Given an array A of N non-negative numbers and you are also given non-negative number B.
#You need to find the number of subarrays in A having sum less than B. We may assume that there is no overflow.
# Input A = [2, 5, 6] B = 10
# output 4
# The subarrays with sum less than B are {2}, {5}, {6} and {2, 5} which is total of 4 Subarrays
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count1=0 # To store the Value 
        for i in range(len(A)): # Two loops to transverse through entire subarrays
            for j in range(i,len(A)):
                sum1=sum(A[i:j+1]) 
                if sum1<B:
                    count1+=1
        return count1