#N light bulbs are connected by a wire. Each bulb has a switch associated with it, however due to faulty wiring, a switch also changes the state of all the bulbs to the right of current bulb.
#Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs.
#You can press the same switch multiple times.
# Note: 0 represents the bulb is off and 1 represents the bulb is on.
#Explanation 1:  A = [0, 1, 0, 1]
# press switch 0 : [1 0 1 0]
# press switch 1 : [1 1 0 1]
# press switch 2 : [1 1 1 0]
# press switch 3 : [1 1 1 1]
# output is 4 

class Solution:
	# @param A : list of integers
	# @return an integer
	def bulbs(self, A):
        res=0
        cnt=0
        if 0 not in A:
            return 0
        
        for i in range(len(A)):
        # if the bulb's original state is off and
        # count is even, it is currently off...
        # press this switch to on the bulb and
        # increase the count
			if (A[i] == 1 and cnt % 2 != 0):
                res += 1
                cnt += 1
	
		
		# if the bulb's original state is on and count
        # is odd, it is currently off...
        # Press this switch to on the bulb and increase
        # the count
            if (A[i] == 0 and cnt % 2 == 0):
                res += 1
                cnt += 1
        return res