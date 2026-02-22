#Given an array of integers A, find and return the product array of same size where i'th eement of the product 
#array will be equal to the product of all the elements divided by the i'th element of the array.
#Input: arr[]  = {10, 3, 5, 6, 2}
#Output: prod[]  = {180, 600, 360, 300, 900}
#3 * 5 * 6 * 2 product of other array 
#elements except 10 is 180
#10 * 5 * 6 * 2 product of other array 
#elements except 3 is 600
#10 * 3 * 6 * 2 product of other array 
#elements except 5 is 360
#10 * 3 * 5 * 2 product of other array 
#elements except 6 is 300
#10 * 3 * 6 * 5 product of other array 
#elements except 2 is 900

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        prod=1
        RP=[None] * len(A)
        for i in A:
            prod=prod*i
        
        for i in range(len(A)):
            RP[i]=prod//A[i]
        return RP
