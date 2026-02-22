# Given an array of integers A, of size N.
#Return the maximum size subarray of A having only non-negative elements. If there are more than one such subarrays, return the one having the earliest starting index in A.
#A = [5, 6, -1, 7, 8]
# output  [5, 6] ( here 7,8 gives the same result but 5 6 appears first 
#There are two subarrays of size 2 having only non-negative elements.
# 1. [5, 6]  starting point  = 0
# 2. [7, 8]  starting point  = 3
# As starting point of 1 is smaller, return [5, 6]

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self,A):
        i=j=prev_i=prev_j=-1
        n=len(A)
        for col in range(n):
                if A[col]>0 and i==-1:
                        i=col
                elif A[col]>0 & i>-1:
                        j=col
                
                elif A[col]<0 :
                    if prev_i==-1 and prev_j==-1:
                        prev_i=i
                        prev_j=j
                    i=-1
                    j=-1
                if (j-i > prev_j-prev_i) and(i>-1 and prev_i>-1):
                    prev_i=i
                    prev_j=j
        
        if prev_j==-1:
            prev_j=prev_i
                    
        return A[prev_i:prev_j+1]