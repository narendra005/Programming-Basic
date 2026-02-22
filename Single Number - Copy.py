#Given an array of numbers A , in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
#Note: Output array must be sorted.
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        counts = dict()
        ans=[]
        
        for i in A:
            counts[i] = counts.get(i, 0)+1 
            temp=counts[i]

        for key,val in counts.items():
            if val==1:
                ans.append(key)
        ans.sort()
        return ans