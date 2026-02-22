# Write a function that takes an integer and returns the number of 1 bits it has.
# 11 is represented as 1011 in binary. so answer is 3

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        count1=0
        while A>0:
            if A%2!=0:
                count1+=1
            A=A//2
        return count1
