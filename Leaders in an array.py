# Given an integer array A containing N distinct integers, you have to find all the leaders in the array A.
#An element is leader if it is strictly greater than all the elements to its right side.
# NOTE:The rightmost element is always a leader.
#Input Format  First and only argument is an integer array A.
# Output Format Return an integer array denoting all the leader elements of the array.
#NOTE: Ordering in the output doesn't matter.
# Example Input  A = [16, 17, 4, 3, 5, 2] Input 2: A = [1, 2]
# Example Output Output 1: [17, 2, 5] Output 2: [2]
#Explanation 1:
#Element 17 is strictly greater than all the elements on the right side to it.
# Element 2 is strictly greater than all the elements on the right side to it.
# Element 5 is strictly greater than all the elements on the right side to it.
# So we will return this three elements i.e [17, 2, 5], we can also return [2, 5, 17] or [5, 2, 17] or any other ordering.


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n=len(A) -1
        ans=[]
        max1=0
        for i in range(n,-1,-1):
            if i==n:
                ans.append(A[i])
                max1=A[i]
            elif (A[i]>max1):
                ans.append(A[i])
                max1=max(A[i],max1)
                #print(max1,end=" ")
        return ans  