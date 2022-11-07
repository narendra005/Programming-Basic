#You are given an array A of size N. You want to convert the array into an Arithmetic Progression with common difference B. Formally, you want that -
#A[i] - A[i-1] = B for 1 ≤ i < N considering array to be 0 indexed.
#Your task is to replace minimum numbers in A so that it forms an Arithmetic Progression.
#Problem Constraints
#1 <= N <= 105
#1 <= A[i] <= 2 x 109
#0 <= B <= 104
#Input Format
#The first argument contains an integer array A of size N.
#The second argument contains an integer B.
#Output Format
#Return the minimum numbers that should be replaced for A to form an Arithmetic Progression.
#Example Input
#Input 1:
#  A : [5, 7, 8, 15]
#  B : 4
#Input 2:
#  A : [1, 2, 1]
#  B : 1
#Example Output
#Output 1:
#  2
#Output 2:
# 1
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        D1={}
        max1=0
        for i in range(len(A)):
            temp=(A[i] - i * B)
            if temp in D1:
                D1[temp]+=1
            else:
                D1[temp]=1
            max1=max(D1[temp],max1)
        
        return len(A) - max1