# Program to find number of zero in a factorial of number
# Only Input is number 
# out is total zero in number for equal 5!=120 will return 1 zero
class Solution:
	# @param A : integer
	# @return an integer
	def trailZ(A):
		n=5
		no_zero=0
		while(A>n):
			i=A//n
			no_zero=no_zero+i
			n=n*5
		return no_zero