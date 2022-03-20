# Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals p.
# Input 1: A = [3, 2, 1, 3]  Input 2: A = [1, 1, 3, 3]
# Output 1 =1 output2= -1

class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
        A.sort(reverse=True)
        count1=cost=0
        if A[0]==0:
            return 1
        for i in range(1,len(A)):
            if A[i]!=A[i-1]:
                cost=i
    
            else:
                if A[i]==A[i-1]:
                    cost=-10**9
                else:
                    cost=i-1

                
            if cost==A[i] :
                count1+=1
        return (1 if count1>0 else -1)