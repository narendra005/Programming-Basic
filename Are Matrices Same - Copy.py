#You are given two two matrices A & B of equal sizes and you have to check whether two matrices are equal or not.
#NOTE: Both matrices are equal if A[i][j] == B[i][j] for all i and j in the given range.
# if equal return 1 else return 0 
# Input 1:
#A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
#B = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
#Input 2: A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
#         B = [[1, 2, 3],[7, 8, 9],[4, 5, 6]]

#Example Output
#Output 1:1
#Output 2:0



class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        n=len(A)
        for i in range(n):
            if A[i]!=B[i]:
                return 0
        return 1