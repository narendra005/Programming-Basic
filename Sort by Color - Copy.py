#Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#Note: Using library sort function is not allowed.


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sortColors(self, A):
        B=[]
        D={}
        for ix,val in enumerate(A):
            if val not in D:
                D[val]=1
            else:
                D[val]+=1

        for key in sorted (D.keys()):
            temp=D[key]
            while temp>0:
                B.append(key)
                temp=temp-1
        return B