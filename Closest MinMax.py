#Given an array A. Find the size of the smallest subarray such that it contains atleast one occurrence of the maximum value of the array
#and atleast one occurrence of the minimum value of the array.
#Return the length of the smallest subarray which has atleast one occurrence of minimum and maximum element of the array
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        minval=min(A)
        maxval=max(A)
        min_pos=0
        max_pos=0
        pos_min, pos_max, ans = -1, -1, maxval
        if minval==maxval:
            return 1
        for i in range(len(A)):
            if A[i] == minval:
                pos_min = i
            elif A[i]==maxval:
                pos_max=i
            
            if (pos_max != -1) and (pos_min != -1):
                ans = min(ans, (abs(pos_min - pos_max) + 1))
        return ans

