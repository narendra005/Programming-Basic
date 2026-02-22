#Given an integer array A of size N.
#You have to find all possible non-empty subsequence of the array of numbers and then, for each subsequence, find the difference between the largest and smallest numbers in that subsequence Then add up all the differences to get the number.
#As the number may be large, output the number modulo 1e9 + 7 (1000000007).
#NOTE: Subsequence can be non-contiguous.
#All possible non-empty subsets are:
#[1]    largest-smallest = 1 - 1 = 0
#[2]    largest-smallest = 2 - 2 = 0
#[1 2]  largest-smallest = 2 - 1 = 1
#Sum of the differences = 0 + 0 + 1 = 1
#So, the resultant number is 1
class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
        A.sort()
        max_sum=min_sum=0
        n=len(A)-1
        mod = 1000000007
        temp=0
        for i in range(len(A)):
            power=2**i % mod
            max_sum=((A[i] * power)% mod) + max_sum
            min_sum=((A[n] * power)% mod) + min_sum
            n-=1
        return ((max_sum-min_sum)%mod+mod)%mod # +mod is to cater to negative situation which arise when we mod with smaller number

        
